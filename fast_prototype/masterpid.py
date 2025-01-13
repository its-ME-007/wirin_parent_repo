from fastapi import APIRouter, HTTPException
from typing import Dict, Union

# Create the FastAPI router
master_pid_values_router = APIRouter()

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

# Endpoint to set PID values
@master_pid_values_router.post('/controlsettings/masterpidvalues/{component}/{value}')
async def set_master_pid_values(component: str, value: int):
    if component in status["ControlSettings"]["MasterPIDValues"]:
        if component in ["SteeringPIDOutput", "BrakePIDOutput"]:
            if -1024 <= value <= 1024:
                status["ControlSettings"]["MasterPIDValues"][component] = value
                return {"status": f"{component} is now {value}"}
        elif component in ["MotorRPIDOutput", "MotorLPIDOutput"]:
            if 0 <= value <= 5000:
                status["ControlSettings"]["MasterPIDValues"][component] = value
                return {"status": f"{component} is now {value}"}
        elif component == "MasterPIDCommandOutput":
            if 0 <= value <= 1000:
                status["ControlSettings"]["MasterPIDValues"][component] = value
                return {"status": f"{component} is now {value}"}
    raise HTTPException(status_code=400, detail="Invalid component or value")

# Endpoint to get PID values
@master_pid_values_router.get('/controlsettings/masterpidvalues/{component}')
async def get_master_pid_values(component: str):
    if component in status["ControlSettings"]["MasterPIDValues"]:
        return {component: status["ControlSettings"]["MasterPIDValues"][component]}
    raise HTTPException(status_code=400, detail="Invalid component")
