import uvicorn
import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from concurrent.futures import ThreadPoolExecutor
from request_queue_manager import request_queue_manager
from starlette.middleware.base import BaseHTTPMiddleware
import json

# Import routers (equivalent of blueprints in Flask)
from intlight import int_lighting_router
from obc import obc_router
from extlight import ext_lighting_router
from cardata1 import cardata1_router
from cardata2 import cardata2_router
from cardata3 import cardata3_router
from cardata4 import cardata4_router, update_globalclock
from tablestat import table_router
from llc import control_settings_router
from pidstatus import pid_status_router
from masterpid import master_pid_values_router
from vehicledoors import door_router
from bywiresystem import bywire_router
from Tv import tv_router
from hvac import hvac_router
from lvl1_cu import lvl1_cu_router
from lvl2_cu import lvl2_cu_router
from carmode import carmode_router
from tyre import tyre_router
from seatf import seat_router
from bmsf import bms_router

class QueueMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        
        # Only queue POST requests
        if request.method == "POST":
            try:
                # Get the response data
                response_body = b""
                async for chunk in response.body_iterator:
                    response_body += chunk
                
                # Decode and queue the response
                response_data = response_body.decode()
                await request_queue_manager.add_request(response_data)
                print(f"Successfully queued response: {response_data}")
                
                # Create a new response with the same data
                return JSONResponse(
                    content=json.loads(response_data),
                    status_code=response.status_code,
                    headers=dict(response.headers)
                )
            except Exception as e:
                print(f"Error in middleware: {str(e)}")
                
        return response

# Main Application
def create_main_app():
    app = FastAPI()
    
    # Add the queue middleware
    app.add_middleware(QueueMiddleware)
    
    # Start the request processor
    @app.on_event("startup")
    async def startup_event():
        asyncio.create_task(request_queue_manager.process_requests())
    
    @app.get("/")
    async def index():
        return {
            "message": "Welcome to the Modular Request Resolver API",
            "port directory": [
                "5000: Main Application",
                "5001: Combined Lighting Application",
                "5002: On-Board Computer (OBC) Application",
                "5003: Car Data Application",
                "5004: Table Statistics Application",
                "5005: Control Settings Application",
                "5006: Vehicle Status Application",
                "5007: Tyre Status Application",
                "5008: Control Unit Status Application",
                "5009: HVAC Application",
                "5010: Seat Status Application",
                "5011: Battery Management System (BMS) Application"
            ]
        }

    @app.exception_handler(404)
    async def not_found_exception_handler(request: Request, exc):
        return JSONResponse(status_code=404, content={"error": "Page not found"})

    # Add this endpoint to check queue status
    @app.get("/queue-status")
    async def get_queue_status():
        return request_queue_manager.get_queue_status()

    return app

# Lighting Application
def create_lighting_app():
    app = FastAPI()
    app.add_middleware(QueueMiddleware)
    app.include_router(int_lighting_router)
    app.include_router(ext_lighting_router)
    return app

# On-Board Computer Application
def create_obc_app():
    app = FastAPI()
    app.include_router(obc_router)
    return app

# Car Data Application
def create_cardata_app():
    app = FastAPI()
    app.include_router(cardata1_router)
    app.include_router(cardata2_router)
    app.include_router(cardata3_router)
    app.include_router(cardata4_router)
    return app

# Table Statistics Application
def create_table_app():
    app = FastAPI()
    app.include_router(table_router)
    return app

# Control Settings Application
def create_controlsettings_app():
    app = FastAPI()
    app.include_router(control_settings_router)
    app.include_router(master_pid_values_router)
    app.include_router(pid_status_router)
    return app

# Vehicle Status Application
def create_vehiclestatus_app():
    app = FastAPI()
    app.include_router(door_router)
    app.include_router(tv_router)
    app.include_router(bywire_router)
    app.include_router(carmode_router)
    return app

# Tyre Status Application
def create_tyre_app():
    app = FastAPI()
    app.include_router(tyre_router)
    return app

# Control Unit Status Application
def create_controlunitstatus_app():
    app = FastAPI()
    app.include_router(lvl1_cu_router)
    app.include_router(lvl2_cu_router)
    return app

# HVAC Application
def create_hvac_app():
    app = FastAPI()
    app.add_middleware(QueueMiddleware)
    app.include_router(hvac_router)
    return app

# Seat Status Application
def create_seat_app():
    app = FastAPI()
    app.include_router(seat_router)
    return app

# Battery Management System Application
def create_bms_app():
    app = FastAPI()
    app.include_router(bms_router)
    return app

# Starting all the applications using ThreadPoolExecutor for batch processing
def start_services():
    apps = [
        (create_main_app(), 5000),
        (create_lighting_app(), 5001),
        (create_obc_app(), 5002),
        (create_cardata_app(), 5003),
        (create_table_app(), 5004),
        (create_controlsettings_app(), 5005),
        (create_vehiclestatus_app(), 5006),
        (create_tyre_app(), 5007),
        (create_controlunitstatus_app(), 5008),
        (create_hvac_app(), 5009),
        (create_seat_app(), 5010),
        (create_bms_app(), 5011)
    ]

    # Use ThreadPoolExecutor for batch processing
    with ThreadPoolExecutor(max_workers=len(apps)) as executor:
        for app, port in apps:
            executor.submit(uvicorn.run, app, host="127.0.0.1", port=port)

if __name__ == "__main__":
    start_services()
