from fastapi import APIRouter, HTTPException

cardata2_router = APIRouter()

status = {
    "ihumidity": 0,
    "itemperature": 0,
}

def check_limits(value, min_val, max_val, name):
    if value < min_val or value > max_val:
        raise HTTPException(status_code=400, detail=f"{name} value {value} is out of range ({min_val} to {max_val})")

@cardata2_router.post("/ihumidity/post")
async def ihumidity_post(ihumidity: int):
    check_limits(ihumidity, 0, 100, "ihumidity")
    status["ihumidity"] = ihumidity
    return {"ihumidity": status["ihumidity"]}

@cardata2_router.get("/ihumidity/get")
async def ihumidity_get():
    return {"ihumidity": status["ihumidity"]}

@cardata2_router.post("/itemperature/post")
async def itemperature_post(itemperature: int):
    check_limits(itemperature, 0, 100, "itemperature")
    status["itemperature"] = itemperature
    return {"itemperature": status["itemperature"]}

@cardata2_router.get("/itemperature/get")
async def itemperature_get():
    return {"itemperature": status["itemperature"]}
