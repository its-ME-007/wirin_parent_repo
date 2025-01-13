from fastapi import FastAPI, HTTPException, APIRouter, Query
from typing import Optional

app = FastAPI()
int_lighting_router = APIRouter()

status = {
    "Internal": {
        "RoofLight": {"Status": 0, "Brightness": 0},
        "DoorPuddleLights": {"Status": 0, "Brightness": 0},
        "FloorLights": {"Status": 0, "Brightness": 0},
        "DashboardLights": {"Status": 0, "Brightness": 0},
        "BootLights": {"Status": 0}
    }
}

# RoofLight Endpoints
@int_lighting_router.post('/internal/rooflight/status')
async def set_internal_rooflight_status(Status: str = Query(...)):
    status_map = {"ON": 1, "OFF": 0}
    if Status not in status_map:
        raise HTTPException(status_code=400, detail="Invalid Status. Use 'ON' or 'OFF'")
    status["Internal"]["RoofLight"]["Status"] = status_map[Status]
    return {"component": "RoofLight", "property": "Status", "value": status_map[Status]}

@int_lighting_router.get('/internal/rooflight/status')
async def get_internal_rooflight_status():
    return {"component": "RoofLight", "property": "Status", "value": status["Internal"]["RoofLight"]["Status"]}

@int_lighting_router.post('/internal/rooflight/brightness')
async def set_internal_rooflight_brightness(Brightness: int = Query(...)):
    if not 0 <= Brightness <= 100:
        raise HTTPException(status_code=400, detail="Invalid Brightness")
    status["Internal"]["RoofLight"]["Brightness"] = Brightness
    return {"component": "RoofLight", "property": "Brightness", "value": Brightness}

@int_lighting_router.get('/internal/rooflight/brightness')
async def get_internal_rooflight_brightness():
    return {"component": "RoofLight", "property": "Brightness", "value": status["Internal"]["RoofLight"]["Brightness"]}

# DoorPuddleLights Endpoints
@int_lighting_router.post('/internal/doorpuddlelights/status')
async def set_internal_doorpuddlelights_status(Status: str = Query(...)):
    status_map = {"ON": 1, "OFF": 0}
    if Status not in status_map:
        raise HTTPException(status_code=400, detail="Invalid Status. Use 'ON' or 'OFF'")
    status["Internal"]["DoorPuddleLights"]["Status"] = status_map[Status]
    return {"component": "DoorPuddleLights", "property": "Status", "value": status_map[Status]}

@int_lighting_router.get('/internal/doorpuddlelights/status')
async def get_internal_doorpuddlelights_status():
    return {"component": "DoorPuddleLights", "property": "Status", "value": status["Internal"]["DoorPuddleLights"]["Status"]}

@int_lighting_router.post('/internal/doorpuddlelights/brightness')
async def set_internal_doorpuddlelights_brightness(Brightness: int = Query(...)):
    if not 0 <= Brightness <= 100:
        raise HTTPException(status_code=400, detail="Invalid Brightness")
    status["Internal"]["DoorPuddleLights"]["Brightness"] = Brightness
    return {"component": "DoorPuddleLights", "property": "Brightness", "value": Brightness}

@int_lighting_router.get('/internal/doorpuddlelights/brightness')
async def get_internal_doorpuddlelights_brightness():
    return {"component": "DoorPuddleLights", "property": "Brightness", "value": status["Internal"]["DoorPuddleLights"]["Brightness"]}

# FloorLights Endpoints
@int_lighting_router.post('/internal/floorlights/status')
async def set_internal_floorlights_status(Status: str = Query(...)):
    status_map = {"ON": 1, "OFF": 0}
    if Status not in status_map:
        raise HTTPException(status_code=400, detail="Invalid Status. Use 'ON' or 'OFF'")
    status["Internal"]["FloorLights"]["Status"] = status_map[Status]
    return {"component": "FloorLights", "property": "Status", "value": status_map[Status]}

@int_lighting_router.get('/internal/floorlights/status')
async def get_internal_floorlights_status():
    return {"component": "FloorLights", "property": "Status", "value": status["Internal"]["FloorLights"]["Status"]}

@int_lighting_router.post('/internal/floorlights/brightness')
async def set_internal_floorlights_brightness(Brightness: int = Query(...)):
    if not 0 <= Brightness <= 100:
        raise HTTPException(status_code=400, detail="Invalid Brightness")
    status["Internal"]["FloorLights"]["Brightness"] = Brightness
    return {"component": "FloorLights", "property": "Brightness", "value": Brightness}

@int_lighting_router.get('/internal/floorlights/brightness')
async def get_internal_floorlights_brightness():
    return {"component": "FloorLights", "property": "Brightness", "value": status["Internal"]["FloorLights"]["Brightness"]}

# DashboardLights Endpoints
@int_lighting_router.post('/internal/dashboardlights/status')
async def set_internal_dashboardlights_status(Status: str = Query(...)):
    status_map = {"ON": 1, "OFF": 0}
    if Status not in status_map:
        raise HTTPException(status_code=400, detail="Invalid Status. Use 'ON' or 'OFF'")
    status["Internal"]["DashboardLights"]["Status"] = status_map[Status]
    return {"component": "DashboardLights", "property": "Status", "value": status_map[Status]}

@int_lighting_router.get('/internal/dashboardlights/status')
async def get_internal_dashboardlights_status():
    return {"component": "DashboardLights", "property": "Status", "value": status["Internal"]["DashboardLights"]["Status"]}

@int_lighting_router.post('/internal/dashboardlights/brightness')
async def set_internal_dashboardlights_brightness(Brightness: int = Query(...)):
    if not 0 <= Brightness <= 100:
        raise HTTPException(status_code=400, detail="Invalid Brightness")
    status["Internal"]["DashboardLights"]["Brightness"] = Brightness
    return {"component": "DashboardLights", "property": "Brightness", "value": Brightness}

@int_lighting_router.get('/internal/dashboardlights/brightness')
async def get_internal_dashboardlights_brightness():
    return {"component": "DashboardLights", "property": "Brightness", "value": status["Internal"]["DashboardLights"]["Brightness"]}

# BootLights Endpoints
@int_lighting_router.post('/internal/bootlights/status')
async def set_internal_bootlights_status(Status: str = Query(...)):
    status_map = {"ON": 1, "OFF": 0}
    if Status not in status_map:
        raise HTTPException(status_code=400, detail="Invalid Status. Use 'ON' or 'OFF'")
    status["Internal"]["BootLights"]["Status"] = status_map[Status]
    return {"component": "BootLights", "property": "Status", "value": status_map[Status]}

@int_lighting_router.get('/internal/bootlights/status')
async def get_internal_bootlights_status():
    return {"component": "BootLights", "property": "Status", "value": status["Internal"]["BootLights"]["Status"]}

# Get all internal lighting status
@int_lighting_router.get('/internal/status')
async def get_internal_lighting_status():
    return status["Internal"]

app.include_router(int_lighting_router)
