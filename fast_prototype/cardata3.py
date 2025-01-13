from fastapi import APIRouter, HTTPException

cardata3_router = APIRouter()

status = {
    "CAN1Stat": "Active",
    "CAN2Stat": "Active",
    "CAN3Stat": "Active",
    "Internet": "Active",
    "Ethernet": "Active"
}

@cardata3_router.post("/can/{num}/stat/post")
async def can_stat_post(num: str, Status: str):
    if num in ["1", "2", "3"]:
        status[f"CAN{num}Stat"] = Status
        return {f"CAN{num}Stat": status[f"CAN{num}Stat"]}
    else:
        raise HTTPException(status_code=400, detail="Invalid CAN number")

@cardata3_router.get("/can/{num}/stat/get")
async def can_stat_get(num: str):
    if num in ["1", "2", "3"]:
        return {f"CAN{num}Stat": status[f"CAN{num}Stat"]}
    else:
        raise HTTPException(status_code=400, detail="Invalid CAN number")

@cardata3_router.post("/internet/post")
async def internet_post(Internet: str):
    status["Internet"] = Internet
    return {"Internet": status["Internet"]}

@cardata3_router.get("/internet/get")
async def internet_get():
    return {"Internet": status["Internet"]}

@cardata3_router.post("/ethernet/post")
async def ethernet_post(Ethernet: str):
    status["Ethernet"] = Ethernet
    return {"Ethernet": status["Ethernet"]}

@cardata3_router.get("/ethernet/get")
async def ethernet_get():
    return {"Ethernet": status["Ethernet"]}
