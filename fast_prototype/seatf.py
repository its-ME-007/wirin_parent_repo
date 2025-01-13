from fastapi import APIRouter, HTTPException
from typing import Dict

# Create the FastAPI router
seat_router = APIRouter()

# Define the status dictionary to keep track of the states
status = {
    "Seat": {
        "CaptainSeat": {
            "FacingPosition": "Front",
            "BackrestPosition": 0
        },
        "CoCaptainSeat": {
            "FacingPosition": "Front",
            "BackrestPosition": 0
        }
    }
}

@seat_router.post('/seat/captain/facingposition/{position}')
async def set_captain_seat_facing_position(position: str):
    if position in ["Front", "Side", "Back", "Rotating"]:
        status["Seat"]["CaptainSeat"]["FacingPosition"] = position
        return {"status": f"Captain seat facing position is now {position}"}
    raise HTTPException(status_code=400, detail="Invalid facing position value")

@seat_router.get('/seat/captain/facingposition')
async def get_captain_seat_facing_position():
    return {"FacingPosition": status["Seat"]["CaptainSeat"]["FacingPosition"]}

@seat_router.post('/seat/captain/backrestposition/{value}')
async def set_captain_seat_backrest_position(value: int):
    if 0 <= value <= 100:
        status["Seat"]["CaptainSeat"]["BackrestPosition"] = value
        return {"status": f"Captain seat backrest position is now {value}%"}
    raise HTTPException(status_code=400, detail="Invalid backrest position value")

@seat_router.get('/seat/captain/backrestposition')
async def get_captain_seat_backrest_position():
    return {"BackrestPosition": status["Seat"]["CaptainSeat"]["BackrestPosition"]}

@seat_router.post('/seat/cocaptain/facingposition/{position}')
async def set_co_captain_seat_facing_position(position: str):
    if position in ["Front", "Side", "Back", "Rotating"]:
        status["Seat"]["CoCaptainSeat"]["FacingPosition"] = position
        return {"status": f"Co-captain seat facing position is now {position}"}
    raise HTTPException(status_code=400, detail="Invalid facing position value")

@seat_router.get('/seat/cocaptain/facingposition')
async def get_co_captain_seat_facing_position():
    return {"FacingPosition": status["Seat"]["CoCaptainSeat"]["FacingPosition"]}

@seat_router.post('/seat/cocaptain/backrestposition/{value}')
async def set_co_captain_seat_backrest_position(value: int):
    if 0 <= value <= 100:
        status["Seat"]["CoCaptainSeat"]["BackrestPosition"] = value
        return {"status": f"Co-captain seat backrest position is now {value}%"}
    raise HTTPException(status_code=400, detail="Invalid backrest position value")

@seat_router.get('/seat/cocaptain/backrestposition')
async def get_co_captain_seat_backrest_position():
    return {"BackrestPosition": status["Seat"]["CoCaptainSeat"]["BackrestPosition"]}

@seat_router.get('/status/seat')
async def get_seat_status():
    return status["Seat"]
