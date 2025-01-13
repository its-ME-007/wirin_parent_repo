from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Create the FastAPI router
control_settings_router = APIRouter()

# Define the status dictionary to keep track of the states
status = {
    "ControlSettings": {
        "LowLevelControlMode": "Manual Mode",
        "PIDStatus": {
            "MasterControl": "OFF",
            "SteeringRack": "OFF",
            "Brake": "OFF",
            "Motors": "OFF"
        },
        "MasterPIDValues": {
            "SteeringPIDOutput": 0,
            "BrakePIDOutput": 0,
            "MotorRPIDOutput": 0,
            "MotorLPIDOutput": 0,
            "MasterPIDCommandOutput": 0
        }
    }
}

# Endpoint to set the low-level control mode
@control_settings_router.post('/controlsettings/lowlevelcontrolmode/{mode}')
async def set_low_level_control_mode(mode: str):
    valid_modes = [
        "Autonomous LEVEL 5", "Autonomous LEVEL 4", "Autonomous LEVEL 3",
        "Autonomous LEVEL 2", "Autonomous LEVEL 1", "Manual Mode", "Hardware Mode"
    ]
    if mode in valid_modes:
        status["ControlSettings"]["LowLevelControlMode"] = mode
        return {"status": f"Low Level Control Mode is now {mode}"}
    raise HTTPException(status_code=400, detail="Invalid mode")

# Endpoint to get the current low-level control mode
@control_settings_router.get('/controlsettings/lowlevelcontrolmode')
async def get_low_level_control_mode():
    return {"LowLevelControlMode": status["ControlSettings"]["LowLevelControlMode"]}
