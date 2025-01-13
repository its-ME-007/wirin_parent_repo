from fastapi import APIRouter, FastAPI

app = FastAPI()

# Create the router with the label 'door_router'
door_router = APIRouter()

# Define the status variables
door_status = "Closed"
boot_door_status = "Closed"
roof_door_status = "Closed"

# Endpoints for Door Status
@door_router.post("/vehicledoors/door/open")
async def open_door():
    global door_status
    door_status = "Open"
    return {"message": "DoorStatus is now Open"}

@door_router.post("/vehicledoors/door/close")
async def close_door():
    global door_status
    door_status = "Closed"
    return {"message": "DoorStatus is now Closed"}

@door_router.post("/vehicledoors/door/opening")
async def opening_door():
    global door_status
    door_status = "Opening"
    return {"message": "DoorStatus is now Opening"}

@door_router.post("/vehicledoors/door/closing")
async def closing_door():
    global door_status
    door_status = "Closing"
    return {"message": "DoorStatus is now Closing"}

@door_router.post("/vehicledoors/door/error")
async def error_door():
    global door_status
    door_status = "Error"
    return {"message": "DoorStatus is now Error"}

@door_router.get("/vehicledoors/door")
async def get_door_status():
    return {"DoorStatus": door_status}

# Endpoints for Boot Door Status
@door_router.post("/vehicledoors/bootdoor/open")
async def open_boot_door():
    global boot_door_status
    boot_door_status = "Open"
    return {"message": "BootDoorStatus is now Open"}

@door_router.post("/vehicledoors/bootdoor/close")
async def close_boot_door():
    global boot_door_status
    boot_door_status = "Closed"
    return {"message": "BootDoorStatus is now Closed"}

@door_router.post("/vehicledoors/bootdoor/opening")
async def opening_boot_door():
    global boot_door_status
    boot_door_status = "Opening"
    return {"message": "BootDoorStatus is now Opening"}

@door_router.post("/vehicledoors/bootdoor/closing")
async def closing_boot_door():
    global boot_door_status
    boot_door_status = "Closing"
    return {"message": "BootDoorStatus is now Closing"}

@door_router.post("/vehicledoors/bootdoor/error")
async def error_boot_door():
    global boot_door_status
    boot_door_status = "Error"
    return {"message": "BootDoorStatus is now Error"}

@door_router.get("/vehicledoors/bootdoor")
async def get_boot_door_status():
    return {"BootDoorStatus": boot_door_status}

# Endpoints for Roof Door Status
@door_router.post("/vehicledoors/roofdoor/open")
async def open_roof_door():
    global roof_door_status
    roof_door_status = "Open"
    return {"message": "RoofDoorStatus is now Open"}

@door_router.post("/vehicledoors/roofdoor/close")
async def close_roof_door():
    global roof_door_status
    roof_door_status = "Closed"
    return {"message": "RoofDoorStatus is now Closed"}

@door_router.post("/vehicledoors/roofdoor/opening")
async def opening_roof_door():
    global roof_door_status
    roof_door_status = "Opening"
    return {"message": "RoofDoorStatus is now Opening"}

@door_router.post("/vehicledoors/roofdoor/closing")
async def closing_roof_door():
    global roof_door_status
    roof_door_status = "Closing"
    return {"message": "RoofDoorStatus is now Closing"}

@door_router.post("/vehicledoors/roofdoor/error")
async def error_roof_door():
    global roof_door_status
    roof_door_status = "Error"
    return {"message": "RoofDoorStatus is now Error"}

@door_router.get("/vehicledoors/roofdoor")
async def get_roof_door_status():
    return {"RoofDoorStatus": roof_door_status}

