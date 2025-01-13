from fastapi import APIRouter, HTTPException
from datetime import datetime
import asyncio

cardata4_router = APIRouter()

status = {
    "Globalclock": "",
    "Distance_to_empty": 100,
    "DistTravelled": 0,
    "DriveMode": "PARKED"
}

def check_limits(value, min_val, max_val, name):
    if value < min_val or value > max_val:
        raise HTTPException(status_code=400, detail=f"{name} value {value} is out of range ({min_val} to {max_val})")
    return None

@cardata4_router.get("/globalclock/get")
async def globalclock_get():
    return {"Globalclock": status["Globalclock"]}

@cardata4_router.post("/distance_to_empty/post")
async def distance_to_empty_post(Distance_to_empty: int):
    check_limits(Distance_to_empty, 0, 100, "Distance_to_empty")
    status["Distance_to_empty"] = Distance_to_empty
    return {"Distance_to_empty": status["Distance_to_empty"]}

@cardata4_router.get("/distance_to_empty/get")
async def distance_to_empty_get():
    return {"Distance_to_empty": status["Distance_to_empty"]}

@cardata4_router.post("/disttravelled/post")
async def disttravelled_post(DistTravelled: int):
    check_limits(DistTravelled, 0, 1000, "DistTravelled")
    status["DistTravelled"] = DistTravelled
    return {"DistTravelled": status["DistTravelled"]}

@cardata4_router.get("/disttravelled/get")
async def disttravelled_get():
    return {"DistTravelled": status["DistTravelled"]}

@cardata4_router.post("/drivemode/post")
async def drivemode_post(DriveMode: str):
    if DriveMode not in ["PARKED", "DRIVING", "REVERSE"]:
        raise HTTPException(status_code=400, detail="Invalid DriveMode")
    status["DriveMode"] = DriveMode
    return {"DriveMode": status["DriveMode"]}

@cardata4_router.get("/drivemode/get")
async def drivemode_get():
    return {"DriveMode": status["DriveMode"]}

async def update_globalclock():
    while True:
        status["Globalclock"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await asyncio.sleep(1)
