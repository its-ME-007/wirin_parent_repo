# tv_router.py
from fastapi import APIRouter, HTTPException

tv_router = APIRouter()

# Define the state and status with default values
tv_state_level = "State1"
tv_status = "Moving Up"

@tv_router.post("/statelevel/set")
async def set_tv_state_level(level: str):
    global tv_state_level
    
    # Validate the state level
    if level not in ["State1", "State2", "State3"]:
        raise HTTPException(status_code=400, detail="Invalid state level")
    
    tv_state_level = level
    return {"result": f"Setting TV state level to {level}"}

@tv_router.get("/statelevel/get")
async def get_tv_state_level():
    return {"result": f"Current TV state level is {tv_state_level}"}

@tv_router.post("/status/set")
async def set_tv_status(state: str):
    global tv_status
    
    # Validate the TV status
    if state not in ["Moving Up", "Moving Down", "State1", "State2", "State3", "Error"]:
        raise HTTPException(status_code=400, detail="Invalid TV status")
    
    tv_status = state
    return {"result": f"Setting TV status to {state}"}

@tv_router.get("/status/get")
async def get_tv_status():
    return {"result": f"Current TV status is {tv_status}"}
