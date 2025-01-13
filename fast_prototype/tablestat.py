from fastapi import APIRouter, HTTPException, Query
from typing import Optional

# Create the FastAPI router
table_router = APIRouter()

# Define the status dictionary to keep track of the states
status = {
    "TableStat": {
        "tableheight": 0,
        "tablestatus": "Closed",
        "tablelamp": 0,
        "tablelampbrightness": 0
    }
}

def check_limits(value: int, min_val: int, max_val: int, name: str):
    if value < min_val or value > max_val:
        raise HTTPException(status_code=400, detail=f"{name} value {value} is out of range ({min_val} to {max_val})")

@table_router.post('/Tablestatus/tableheight')
async def table_height_post(tableheight: int):
    check_limits(tableheight, 0, 100, "tableheight")
    status["TableStat"]["tableheight"] = tableheight
    return {"tableheight": tableheight}

@table_router.get('/Tablestatus/tableheight')
async def table_height_get():
    return {"tableheight": status["TableStat"]["tableheight"]}

@table_router.post('/Tablestatus/table')
async def table_post(tablestatus: str):
    if tablestatus not in ["Open", "Closed", "Opening", "Closing", "Error"]:
        raise HTTPException(status_code=400, detail="Invalid tablestatus value")
    status["TableStat"]["tablestatus"] = tablestatus
    return {"tablestatus": tablestatus}

@table_router.get('/Tablestatus/table')
async def table_get():
    return {"tablestatus": status["TableStat"]["tablestatus"]}

@table_router.post('/Tablestatus/tablelamp')
async def table_lamp_post(tablelamp: int):
    if tablelamp not in [0, 1]:
        raise HTTPException(status_code=400, detail="Invalid tablelamp value, must be 0 (off) or 1 (on)")
    status["TableStat"]["tablelamp"] = tablelamp
    tablelamp_status = "on" if tablelamp == 1 else "off"
    return {"tablelamp": tablelamp, "tablelamp_status": tablelamp_status}

@table_router.get('/Tablestatus/tablelamp')
async def table_lamp_get():
    tablelamp_status = "on" if status["TableStat"]["tablelamp"] == 1 else "off"
    return {"tablelamp_status": tablelamp_status}

@table_router.post('/Tablestatus/tablelampbrightness')
async def table_lamp_brightness_post(tablelampbrightness: int):
    check_limits(tablelampbrightness, 0, 100, "tablelampbrightness")
    status["TableStat"]["tablelampbrightness"] = tablelampbrightness
    return {"tablelampbrightness": tablelampbrightness}

@table_router.get('/Tablestatus/tablelampbrightness')
async def table_lamp_brightness_get():
    return {"tablelampbrightness": status["TableStat"]["tablelampbrightness"]}
