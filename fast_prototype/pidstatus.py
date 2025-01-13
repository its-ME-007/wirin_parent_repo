from fastapi import APIRouter, HTTPException
from typing import Dict

# Create the FastAPI router
pid_status_router = APIRouter()

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

@pid_status_router.post('/controlsettings/pidstatus/{component}/{action}')
async def set_pid_status(component: str, action: str):
    if component in status["ControlSettings"]["PIDStatus"] and action in ["ON", "OFF"]:
        status["ControlSettings"]["PIDStatus"][component] = action
        return {"status": f"{component} is now {action}"}
    raise HTTPException(status_code=400, detail="Invalid component or action")

@pid_status_router.get('/controlsettings/pidstatus/{component}')
async def get_pid_status(component: str):
    if component in status["ControlSettings"]["PIDStatus"]:
        return {component: status["ControlSettings"]["PIDStatus"][component]}
    raise HTTPException(status_code=400, detail="Invalid component")
