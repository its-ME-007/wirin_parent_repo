from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.responses import RedirectResponse
import logging
import datetime

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI()

bms_router = APIRouter()

# Define the status dictionary to keep track of the states
status = {
    "Battery": {
        "Voltage": 0,
        "Current": 0,
        "SOC": 0,
        "NumberOfCells": 0,
        "CellVoltage": 0,
        "ChargingMOSFET": "OFF",
        "DischargingMOSFET": "OFF",
        "CellMinimumVoltage": 0,
        "CellMinVoltageNumber": 0,
        "CellMaximumVoltage": 0,
        "CellMaxVoltageNumber": 0,
        "Capacity": 0,
        "ERRORStatus": 0,
        "Temperature": 0
    }
}

valid_ranges = {
    "voltage": (60, 85),
    "soc": (20, 100),
    "cell_voltage": (2.0, 4.2),
}

@bms_router.post('/battery/{attribute}/{value}')
async def set_battery_attribute(attribute: str, value: float):
    try:
        logger.debug(f"Received request - Attribute: {attribute}, Value: {value}")
        
        # Validate value is a number
        try:
            value = float(value)
        except ValueError:
            logger.error(f"Invalid value format: {value}")
            return RedirectResponse(
                url=f"/error?message=Invalid value format. Must be a number.",
                status_code=303
            )

        # Add validation for individual cell voltages (Voltage_1 to Voltage_24)
        if attribute.lower().startswith("voltage_"):
            logger.debug(f"Validating cell voltage: {value}")
            if not (valid_ranges["cell_voltage"][0] <= value <= valid_ranges["cell_voltage"][1]):
                logger.warning(f"Cell voltage {value}V out of range [{valid_ranges['cell_voltage'][0]}, {valid_ranges['cell_voltage'][1]}]")
                return RedirectResponse(
                    url=f"/error?message=Cell voltage must be between {valid_ranges['cell_voltage'][0]}V and {valid_ranges['cell_voltage'][1]}V",
                    status_code=303
                )
        elif attribute.lower() == "soc":
            logger.debug(f"Validating SOC: {value}")
            if not (valid_ranges["soc"][0] <= value <= valid_ranges["soc"][1]):
                logger.warning(f"SOC {value}% out of range [{valid_ranges['soc'][0]}, {valid_ranges['soc'][1]}]")
                return RedirectResponse(
                    url=f"/error?message=SOC must be between {valid_ranges['soc'][0]}% and {valid_ranges['soc'][1]}%",
                    status_code=303
                )
        elif attribute.lower() == "voltage":
            logger.debug(f"Validating battery voltage: {value}")
            if not (valid_ranges["voltage"][0] <= value <= valid_ranges["voltage"][1]):
                logger.warning(f"Battery voltage {value}V out of range [{valid_ranges['voltage'][0]}, {valid_ranges['voltage'][1]}]")
                return RedirectResponse(
                    url=f"/error?message=Voltage must be between {valid_ranges['voltage'][0]}V and {valid_ranges['voltage'][1]}V",
                    status_code=303
                )
        else:
            logger.warning(f"Unknown attribute: {attribute}")
            return RedirectResponse(
                url=f"/error?message=Unknown attribute: {attribute}",
                status_code=303
            )

        logger.info(f"Validation successful for {attribute}: {value}")
        # ... rest of the existing attribute setting code ...

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        return RedirectResponse(
            url=f"/error?message=An unexpected error occurred: {str(e)}",
            status_code=303
        )

@bms_router.get('/battery/{attribute}')
async def get_battery_attribute(attribute: str):
    attribute_mapping = {
        "voltage": "Voltage",
        "current": "Current",
        "soc": "SOC",
        "numberofcells": "NumberOfCells",
        "cellvoltage": "CellVoltage",
        "chargingmosfet": "ChargingMOSFET",
        "dischargingmosfet": "DischargingMOSFET",
        "cellminimumvoltage": "CellMinimumVoltage",
        "cellminvoltagenumber": "CellMinVoltageNumber",
        "cellmaximumvoltage": "CellMaximumVoltage",
        "cellmaxvoltagenumber": "CellMaxVoltageNumber",
        "capacity": "Capacity",
        "errorstatus": "ERRORStatus",
        "temperature": "Temperature"
    }

    if attribute not in attribute_mapping:
        raise HTTPException(status_code=400, detail="Invalid attribute")

    return {attribute_mapping[attribute]: status["Battery"][attribute_mapping[attribute]]}

@bms_router.get('/error')
async def error_page(message: str):
    logger.error(f"Error page accessed with message: {message}")
    return {
        "error": True,
        "message": message,
        "timestamp": datetime.datetime.now().isoformat(),
        "status": "error"
    }

# Add a debug endpoint to check current ranges
@bms_router.get('/debug/ranges')
async def get_valid_ranges():
    logger.debug("Valid ranges requested")
    return {
        "valid_ranges": valid_ranges,
        "timestamp": datetime.datetime.now().isoformat()
    }

app.include_router(bms_router)
