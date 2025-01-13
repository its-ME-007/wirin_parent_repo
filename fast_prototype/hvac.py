from fastapi import FastAPI, APIRouter, HTTPException

app = FastAPI()
hvac_router = APIRouter()

status = {
    "HVAC": {
        "Temperature": 0,
        "FanSpeed": 0,
        "ACStatus": 0,
        "ACBlowToSeatFrontRight": 0,
        "ACBlowToSeatFrontLeft": 0,
        "ACBlowToSeatRearRight": 0,
        "ACBlowToSeatRearLeft": 0
    }
}

def validate_component(component):
    return component in status["HVAC"]

def validate_value(component, value):
    if not isinstance(value, int):
        return False
    if component == "Temperature" and 0 <= value <= 100:
        return True
    elif component == "FanSpeed" and 0 <= value <= 100:
        return True
    elif component == "ACStatus" and value in (0, 1):
        return True
    elif component in ("ACBlowToSeatFrontRight", "ACBlowToSeatFrontLeft", "ACBlowToSeatRearRight", "ACBlowToSeatRearLeft") and value in (0, 1):
        return True
    return False

@hvac_router.post('/hvac/{component}/{value}')
async def set_hvac_value(component: str, value: int):
    if component not in status["HVAC"]:
        raise HTTPException(status_code=400, detail="Invalid component")
        
    if component == "Temperature" and not 0 <= value <= 100:
        raise HTTPException(status_code=400, detail="Invalid temperature value")
    elif component == "FanSpeed" and not 0 <= value <= 100:
        raise HTTPException(status_code=400, detail="Invalid fan speed value")
    elif component in ["ACStatus", "ACBlowToSeatFrontRight", "ACBlowToSeatFrontLeft", 
                      "ACBlowToSeatRearRight", "ACBlowToSeatRearLeft"] and value not in [0, 1]:
        raise HTTPException(status_code=400, detail="Invalid value for this component")
        
    status["HVAC"][component] = value
    return {"component": component, "property": "value", "value": value}

@hvac_router.get('/hvac/{component}')
async def get_hvac_value(component: str):
    if validate_component(component):
        return {component: status["HVAC"][component]}
    else:
        raise HTTPException(status_code=400, detail="Invalid component")

@hvac_router.get('/status/hvac')
async def get_hvac_status():
    return status["HVAC"]

app.include_router(hvac_router)
