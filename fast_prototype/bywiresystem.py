from fastapi import FastAPI, APIRouter, HTTPException

app = FastAPI()
bywire_router = APIRouter()

steering_status = "Open"
acc_brake_pedal_status = "Open"

@bywire_router.post('/bywiresystem/steering/open')
async def open_steering():
    global steering_status
    steering_status = "Open"
    return {"message": "SteeringStatus is now Open"}, 200

@bywire_router.post('/bywiresystem/steering/close')
async def close_steering():
    global steering_status
    steering_status = "Close"
    return {"message": "SteeringStatus is now Close"}, 200

@bywire_router.post('/bywiresystem/steering/opening')
async def opening_steering():
    global steering_status
    steering_status = "Opening"
    return {"message": "SteeringStatus is now Opening"}, 200

@bywire_router.post('/bywiresystem/steering/closing')
async def closing_steering():
    global steering_status
    steering_status = "Closing"
    return {"message": "SteeringStatus is now Closing"}, 200

@bywire_router.post('/bywiresystem/steering/error')
async def error_steering():
    global steering_status
    steering_status = "Error"
    return {"message": "SteeringStatus is now Error"}, 200

@bywire_router.get('/bywiresystem/steering')
async def get_steering_status():
    return {"steering_status": steering_status}, 200

@bywire_router.post('/bywiresystem/accbrake/open')
async def open_acc_brake():
    global acc_brake_pedal_status
    acc_brake_pedal_status = "Open"
    return {"message": "AccBrakePedalStatus is now Open"}, 200

@bywire_router.post('/bywiresystem/accbrake/close')
async def close_acc_brake():
    global acc_brake_pedal_status
    acc_brake_pedal_status = "Close"
    return {"message": "AccBrakePedalStatus is now Close"}, 200

@bywire_router.post('/bywiresystem/accbrake/opening')
async def opening_acc_brake():
    global acc_brake_pedal_status
    acc_brake_pedal_status = "Opening"
    return {"message": "AccBrakePedalStatus is now Opening"}, 200

@bywire_router.post('/bywiresystem/accbrake/closing')
async def closing_acc_brake():
    global acc_brake_pedal_status
    acc_brake_pedal_status = "Closing"
    return {"message": "AccBrakePedalStatus is now Closing"}, 200

@bywire_router.post('/bywiresystem/accbrake/error')
async def error_acc_brake():
    global acc_brake_pedal_status
    acc_brake_pedal_status = "Error"
    return {"message": "AccBrakePedalStatus is now Error"}, 200

@bywire_router.get('/bywiresystem/accbrake')
async def get_acc_brake_pedal_status():
    return {"acc_brake_pedal_status": acc_brake_pedal_status}, 200


