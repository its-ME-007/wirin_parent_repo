from fastapi import FastAPI, APIRouter, HTTPException

app = FastAPI()
carmode_router = APIRouter()

car_mode = "ENTERTAINMENT_MODE"

@carmode_router.post('/carmode/entertainment')
async def entertainment_mode():
    global car_mode
    car_mode = "ENTERTAINMENT_MODE"
    return {"message": "Car mode is now ENTERTAINMENT_MODE"}, 200

@carmode_router.post('/carmode/ambient')
async def ambient_mode():
    global car_mode
    car_mode = "AMBIENT_MODE"
    return {"message": "Car mode is now AMBIENT_MODE"}, 200

@carmode_router.post('/carmode/focus')
async def focus_mode():
    global car_mode
    car_mode = "FOCUS_MODE"
    return {"message": "Car mode is now FOCUS_MODE"}, 200

@carmode_router.post('/carmode/night')
async def night_mode():
    global car_mode
    car_mode = "NIGHT_MODE"
    return {"message": "Car mode is now NIGHT_MODE"}, 200

@carmode_router.post('/carmode/ride')
async def ride_mode():
    global car_mode
    car_mode = "RIDE_MODE"
    return {"message": "Car mode is now RIDE_MODE"}, 200

@carmode_router.get('/carmode')
async def get_car_mode():
    return {"car_mode": car_mode}, 200

# Register the router with the FastAPI app
app.include_router(carmode_router)
