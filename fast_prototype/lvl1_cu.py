from fastapi import APIRouter, HTTPException
from typing import Union

# Create the FastAPI router
lvl1_cu_router = APIRouter()

# Define the status dictionary to keep track of the states
lvl1_status = {
    "LEVEL1_CU": {
        "ECU2-ICU": {"Heartbeat": 0, "Status": "N/A"},
        "ECU6-VHMS": {"Heartbeat": 0, "Status": "N/A"},
        "17- Monitor and Processor": {"Heartbeat": "N/A", "Status": "ACTIVE/PROCESSING/BUSY"},
        "MPU - Motion Planner": {"Heartbeat": "N/A", "Status": "PROCESSING/ACTIVE/BUSY/OVERLOAD"}
    }
}

# Endpoint to set ECU status
@lvl1_cu_router.post('/controlunitstatus/{ecu}/{attribute}/{value}')
async def set_ecu_status(ecu: str, attribute: str, value: str):
    if ecu in lvl1_status["LEVEL1_CU"]:
        if attribute in lvl1_status["LEVEL1_CU"][ecu]:
            if attribute == "Heartbeat":
                if value == "1":
                    lvl1_status["LEVEL1_CU"][ecu][attribute] = 1
                elif value == "0":
                    lvl1_status["LEVEL1_CU"][ecu][attribute] = 0
                else:
                    raise HTTPException(status_code=400, detail="Invalid heartbeat value")
            else:
                lvl1_status["LEVEL1_CU"][ecu][attribute] = value
            return {"status": f"{ecu} {attribute} is now {value}"}
    raise HTTPException(status_code=400, detail="Invalid ECU or attribute")

# Endpoint to get ECU status
@lvl1_cu_router.get('/controlunitstatus/{ecu}/{attribute}')
async def get_ecu_status(ecu: str, attribute: str):
    if ecu in lvl1_status["LEVEL1_CU"]:
        if attribute in lvl1_status["LEVEL1_CU"][ecu]:
            if attribute == "Heartbeat":
                return {attribute: str(lvl1_status["LEVEL1_CU"][ecu][attribute])}
            return {attribute: lvl1_status["LEVEL1_CU"][ecu][attribute]}
    raise HTTPException(status_code=400, detail="Invalid ECU or attribute")

# Endpoint to retrieve the overall control unit status
@lvl1_cu_router.get('/status/lvl1controlunitstatus')
async def get_lvl1_control_unit_status():
    return {"LEVEL1_CU": lvl1_status["LEVEL1_CU"]}
