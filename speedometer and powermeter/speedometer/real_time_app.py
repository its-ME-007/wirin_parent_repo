from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
import json
import os
import paho.mqtt.client as mqtt
from fastapi.responses import HTMLResponse
from threading import Thread
import asyncio

app = FastAPI()

# Path to the JSON file
json_file_path = "speeddata.json"
speed_value = None  # Store the current speed value
clients = []  # List of connected WebSocket clients

# MQTT Configuration
broker = "localhost"
port = 1883
topic = "speed"


# Load speed from JSON file
def load_speed_from_json():
    global speed_value
    try:
        if os.path.exists(json_file_path):
            with open(json_file_path, "r") as file:
                data = json.load(file)
                if "speed" in data:
                    speed_value = data["speed"]
                    return speed_value
        else:
            raise Exception("JSON file not found.")
    except Exception as e:
        print(f"Error loading JSON file: {e}")


# Update speed in JSON file
def update_speed_in_json(new_speed):
    global speed_value
    speed_value = new_speed
    with open(json_file_path, "w") as file:
        json.dump({"speed": speed_value}, file, indent=4)
    asyncio.run(notify_clients())  # Notify WebSocket clients of the updated speed


# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker")
    client.subscribe(topic)


def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    data = json.loads(payload)
    if "speed" in data:
        new_speed = data["speed"]
        update_speed_in_json(new_speed)
        print(f"Updated speed: {new_speed}")


# Start MQTT Client in a separate thread
def start_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port, 60)
    client.loop_forever()


# WebSocket handling
async def notify_clients():
    for client in clients:
        try:
            await client.send_json({"speed": speed_value})
        except WebSocketDisconnect:
            clients.remove(client)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    await websocket.send_json({"speed": speed_value})  # Send the current speed on connection
    try:
        while True:
            await websocket.receive_text()  # Keep the connection alive
    except WebSocketDisconnect:
        clients.remove(websocket)


# FastAPI route to return the current speed value
@app.get("/speed")
async def get_speed():
    if speed_value is None:
        raise HTTPException(status_code=404, detail="Speed not available")
    return {"speed": speed_value}


# HTML page to demonstrate WebSocket connection
@app.get("/")
async def get():
    html_content = """
    <html>
        <head>
            <title>Speed Monitor</title>
        </head>
        <body>
            <h1>Speed: <span id="speed-value">Loading...</span></h1>
            <script>
                const ws = new WebSocket("ws://localhost:8000/ws");
                ws.onmessage = function(event) {
                    const data = JSON.parse(event.data);
                    document.getElementById("speed-value").innerText = data.speed;
                };
            </script>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)


# Start MQTT in a separate thread
Thread(target=start_mqtt).start()

# Load the initial speed value from the JSON file
load_speed_from_json()
