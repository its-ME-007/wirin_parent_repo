from fastapi import FastAPI, APIRouter, HTTPException, Request
from request_queue_manager import request_queue_manager

app = FastAPI()
ext_lighting_router = APIRouter()

status = {
    "External": {
        "Headlights": {"Status": 0},
        "TailLights": {"Status": 0},
        "BrakeLights": {"Status": 0},
        "TurnSignals": {"Status": 0},
        "FogLights": {"Status": 0}
    }
}

@ext_lighting_router.post('/external/headlights/status/post')
async def set_external_headlights_status(request: Request):
    data = await request.json()
    light_status = data.get("Status")
    if light_status not in [0, 1]:
        raise HTTPException(status_code=400, detail="Invalid Status")
    status["External"]["Headlights"]["Status"] = light_status
    response_data = {
        "component": "Headlights",
        "action": "set_status",
        "value": light_status
    }
    await request_queue_manager.add_request(response_data)
    return {"HeadlightsStatus": status["External"]["Headlights"]["Status"]}

@ext_lighting_router.get('/external/headlights/status/get')
async def get_external_headlights_status():
    return {"HeadlightsStatus": status["External"]["Headlights"]["Status"]}

@ext_lighting_router.post('/external/taillights/status/post')
async def set_external_taillights_status(request: Request):
    data = await request.json()
    light_status = data.get("Status")
    if light_status not in [0, 1]:
        raise HTTPException(status_code=400, detail="Invalid Status")
    status["External"]["TailLights"]["Status"] = light_status
    response_data = {
        "component": "TailLights",
        "action": "set_status",
        "value": light_status
    }
    await request_queue_manager.add_request(response_data)
    return {"TailLightsStatus": status["External"]["TailLights"]["Status"]}

@ext_lighting_router.get('/external/taillights/status/get')
async def get_external_taillights_status():
    return {"TailLightsStatus": status["External"]["TailLights"]["Status"]}

@ext_lighting_router.post('/external/brakelights/status/post')
async def set_external_brakelights_status(request: Request):
    data = await request.json()
    light_status = data.get("Status")
    if light_status not in [0, 1]:
        raise HTTPException(status_code=400, detail="Invalid Status")
    status["External"]["BrakeLights"]["Status"] = light_status
    response_data = {
        "component": "BrakeLights",
        "action": "set_status",
        "value": light_status
    }
    await request_queue_manager.add_request(response_data)
    return {"BrakeLightsStatus": status["External"]["BrakeLights"]["Status"]}

@ext_lighting_router.get('/external/brakelights/status/get')
async def get_external_brakelights_status():
    return {"BrakeLightsStatus": status["External"]["BrakeLights"]["Status"]}

@ext_lighting_router.post('/external/turnsignals/status/post')
async def set_external_turnsignals_status(request: Request):
    data = await request.json()
    light_status = data.get("Status")
    if light_status not in [0, 1]:
        raise HTTPException(status_code=400, detail="Invalid Status")
    status["External"]["TurnSignals"]["Status"] = light_status
    response_data = {
        "component": "TurnSignals",
        "action": "set_status",
        "value": light_status
    }
    await request_queue_manager.add_request(response_data)
    return {"TurnSignalsStatus": status["External"]["TurnSignals"]["Status"]}

@ext_lighting_router.get('/external/turnsignals/status/get')
async def get_external_turnsignals_status():
    return {"TurnSignalsStatus": status["External"]["TurnSignals"]["Status"]}

@ext_lighting_router.post('/external/foglights/status/post')
async def set_external_foglights_status(request: Request):
    data = await request.json()
    light_status = data.get("Status")
    if light_status not in [0, 1]:
        raise HTTPException(status_code=400, detail="Invalid Status")
    status["External"]["FogLights"]["Status"] = light_status
    response_data = {
        "component": "FogLights",
        "action": "set_status",
        "value": light_status
    }
    await request_queue_manager.add_request(response_data)
    return {"FogLightsStatus": status["External"]["FogLights"]["Status"]}

@ext_lighting_router.get('/external/foglights/status/get')
async def get_external_foglights_status():
    return {"FogLightsStatus": status["External"]["FogLights"]["Status"]}

# Register the router with the FastAPI app
app.include_router(ext_lighting_router)
