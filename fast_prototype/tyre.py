# tyre_router.py
from fastapi import APIRouter, HTTPException
from typing import Optional

tyre_router = APIRouter()

# Define the status dictionary to keep track of tyre pressure values
status = {
    "TyrePressure": {
        "front_right_wheel": 0,
        "front_left_wheel": 0,
        "rear_right_wheel": 0,
        "rear_left_wheel": 0
    }
}

def check_limits(value: int, min_val: int, max_val: int, name: str) -> Optional[dict]:
    if value < min_val or value > max_val:
        return {"Error": f"{name} value {value} is out of range ({min_val} to {max_val})"}
    return None

@tyre_router.get("/Tyrepressure/{point}/{side}/get")
async def tyre_pressure_get(point: str, side: str):
    if point == 'F':
        if side == "L":
            pressure = status["TyrePressure"]["front_left_wheel"]
        elif side == "R":
            pressure = status["TyrePressure"]["front_right_wheel"]
        else:
            raise HTTPException(status_code=400, detail="Invalid side")
    elif point == 'B':
        if side == "L":
            pressure = status["TyrePressure"]["rear_left_wheel"]
        elif side == "R":
            pressure = status["TyrePressure"]["rear_right_wheel"]
        else:
            raise HTTPException(status_code=400, detail="Invalid side")
    else:
        raise HTTPException(status_code=400, detail="Invalid point")
    
    return {"Pressure": pressure}

@tyre_router.get("/Tyrepressure/all/get")
async def tyre_pressure_get_all():
    return status["TyrePressure"]
