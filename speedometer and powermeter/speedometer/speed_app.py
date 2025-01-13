from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

# Function to read speed value from JSON file
def get_speed_from_json():
    try:
        with open("speeddata.json", "r") as file:
            data = json.load(file)
            return data.get("speed")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Error reading JSON")

# FastAPI route to return speed value
@app.get("/speed")
async def get_speed():
    speed = get_speed_from_json()
    if speed is None:
        raise HTTPException(status_code=404, detail="Speed not found in JSON file")
    return speed
