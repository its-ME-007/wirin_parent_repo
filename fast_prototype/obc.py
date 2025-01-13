from fastapi import APIRouter, HTTPException
from typing import Dict

# Create the FastAPI router
obc_router = APIRouter()

# Define the status dictionary to keep track of the states
status = {
    "Lighting": {
        "Internal": {
            "RoofLight": {"Status": 0, "Brightness": 0},
            "DoorPuddleLights": {"Status": 0, "Brightness": 0},
            "FloorLights": {"Status": 0, "Brightness": 0},
            "DashboardLights": {"Status": 0, "Brightness": 0},
            "BootLights": {"Status": 0}
        },
        "External": {
            "Headlights": {"Status": 0},
            "TailLights": {"Status": 0},
            "BrakeLights": {"Status": 0},
            "TurnSignals": {"Status": 0},
            "FogLights": {"Status": 0}
        }
    },
    "CarData": {
        "cardata1": {
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
        },
        "cardata2": {
            "ihumidity": 0,
            "itemperature": 0,
        },
        "cardata3": {
            "CAN1Stat": "Active",
            "CAN2Stat": "Active",
            "CAN3Stat": "Active",
            "Internet": "Active",
            "Ethernet": "Active"
        },
        "cardata4": {
            "Globalclock": "",
            "Distance_to_empty": 100,
            "DistTravelled": 0,
            "DriveMode": "PARKED"
        }
    },
    "OBC": {
        "AC_Voltage": 0,
        "AC_Current": 0,
        "AC_Power": 0,
        "Charging_Time": 0,
        "DC_Voltage": 0,
        "DC_Current": 0,
        "OBC_Temperature": 0,
        "OBC_Status": 0
    }
}

# Define endpoints for OBC data
@obc_router.get('/obc/ac_voltage/get')
async def get_ac_voltage():
    return {"AC_Voltage": status["OBC"]["AC_Voltage"]}

@obc_router.get('/obc/ac_current/get')
async def get_ac_current():
    return {"AC_Current": status["OBC"]["AC_Current"]}

@obc_router.get('/obc/ac_power/get')
async def get_ac_power():
    return {"AC_Power": status["OBC"]["AC_Power"]}

@obc_router.get('/obc/charging_time/get')
async def get_charging_time():
    return {"Charging_Time": status["OBC"]["Charging_Time"]}

@obc_router.get('/obc/dc_voltage/get')
async def get_dc_voltage():
    return {"DC_Voltage": status["OBC"]["DC_Voltage"]}

@obc_router.get('/obc/dc_current/get')
async def get_dc_current():
    return {"DC_Current": status["OBC"]["DC_Current"]}

@obc_router.get('/obc/obc_temperature/get')
async def get_obc_temperature():
    return {"OBC_Temperature": status["OBC"]["OBC_Temperature"]}

@obc_router.get('/obc/obc_status/get')
async def get_obc_status():
    return {"OBC_Status": status["OBC"]["OBC_Status"]}
