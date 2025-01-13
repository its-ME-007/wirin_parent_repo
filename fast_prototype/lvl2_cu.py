from fastapi import APIRouter, HTTPException
from typing import Union

# Create the FastAPI router
lvl2_cu_router = APIRouter()

# Define the status dictionary to keep track of the states
lvl2_status = {
    "LEVEL2_CU": {
        "ECU1-VCU": {"Heartbeat": 0, "ActiveSoul": "MAIN/SHADOW"},
        "ECUX-FCU": {"Heartbeat": 0, "Status": "N/A"},
        "ECU3-DoorECU": {"Heartbeat": 0, "ActiveSoul": "MAIN/SHADOW"},
        "ECU4-RPi-OUT": {"Heartbeat": 0, "Status": "N/A"},
        "ECU5-RPi-IN": {"Heartbeat": 0, "Status": "N/A"},
        "ECU7-HVAC": {"Heartbeat": 0, "Status": "N/A"},
        "ECU8-USU": {"Heartbeat": 0, "Status": "N/A"},
        "ECU9-LCU": {"Heartbeat": 0, "Status": "N/A"},
        "ECU10-DashboardECU": {"Heartbeat": 0, "Status": "N/A"},
        "ECU11-TableECU": {"Heartbeat": 0, "Status": "N/A"}
    }
}

# Endpoint to set ECU status
@lvl2_cu_router.post('/controlunitstatus/{ecu}/{attribute}/{value}')
async def set_ecu_status(ecu: str, attribute: str, value: str):
    if ecu in lvl2_status["LEVEL2_CU"]:
        if attribute in lvl2_status["LEVEL2_CU"][ecu]:
            if attribute == "Heartbeat":
                if value == "1":
                    lvl2_status["LEVEL2_CU"][ecu][attribute] = 1
                elif value == "0":
                    lvl2_status["LEVEL2_CU"][ecu][attribute] = 0
                else:
                    raise HTTPException(status_code=400, detail="Invalid heartbeat value")
            else:
                lvl2_status["LEVEL2_CU"][ecu][attribute] = value
            return {"status": f"{ecu} {attribute} is now {value}"}
    raise HTTPException(status_code=400, detail="Invalid ECU or attribute")

# Endpoint to get ECU status
@lvl2_cu_router.get('/controlunitstatus/{ecu}/{attribute}')
async def get_ecu_status(ecu: str, attribute: str):
    if ecu in lvl2_status["LEVEL2_CU"]:
        if attribute in lvl2_status["LEVEL2_CU"][ecu]:
            if attribute == "Heartbeat":
                return {attribute: str(lvl2_status["LEVEL2_CU"][ecu][attribute])}
            return {attribute: lvl2_status["LEVEL2_CU"][ecu][attribute]}
    raise HTTPException(status_code=400, detail="Invalid ECU or attribute")

# Endpoint to retrieve the overall control unit status
@lvl2_cu_router.get('/status/lvl2controlunitstatus')
async def get_lvl2_control_unit_status():
    return {"LEVEL2_CU": lvl2_status["LEVEL2_CU"]}
