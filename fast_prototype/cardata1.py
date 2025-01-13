from fastapi import APIRouter, HTTPException

cardata1_router = APIRouter()

status = {
    "SpeedL": 0,
    "SpeedR": 0,
    "SteeringAngle": 0,
    "BrakeLevel": 0,
    "Gear": "Neutral",
    "FootSwitch": "ON",
    "MotorBrake": "ON",
    "KellyLStatus": 0,
    "KellyRStatus": 0,
    "VehicleError": 0,
}

def check_limits(value, min_val, max_val, name):
    if value < min_val or value > max_val:
        raise HTTPException(status_code=400, detail=f"{name} value {value} is out of range ({min_val} to {max_val})")

@cardata1_router.post("/speed/{side}/post")
async def speed_post(side: str, Speed: int):
    check_limits(Speed, 0, 5000, "Speed")
    if side == "L":
        status["SpeedL"] = Speed
    elif side == "R":
        status["SpeedR"] = Speed
    else:
        raise HTTPException(status_code=400, detail="Invalid side")
    return {"Speed": status[f"Speed{side}"]}

@cardata1_router.get("/speed/{side}/get")
async def speed_get(side: str):
    if side == "L":
        return {"Speed": status["SpeedL"]}
    elif side == "R":
        return {"Speed": status["SpeedR"]}
    else:
        raise HTTPException(status_code=400, detail="Invalid side")

@cardata1_router.post("/steeringangle/post")
async def steeringangle_post(SteeringAngle: int):
    check_limits(SteeringAngle, -30, 30, "SteeringAngle")
    status["SteeringAngle"] = SteeringAngle
    return {"SteeringAngle": status["SteeringAngle"]}

@cardata1_router.get("/steeringangle/get")
async def steeringangle_get():
    return {"SteeringAngle": status["SteeringAngle"]}

@cardata1_router.post("/brakelevel/post")
async def brakelevel_post(BrakeLevel: int):
    check_limits(BrakeLevel, 0, 100, "BrakeLevel")
    status["BrakeLevel"] = BrakeLevel
    return {"BrakeLevel": status["BrakeLevel"]}

@cardata1_router.get("/brakelevel/get")
async def brakelevel_get():
    return {"BrakeLevel": status["BrakeLevel"]}
