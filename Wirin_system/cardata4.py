from flask import Blueprint, jsonify, request
from datetime import datetime
import time

cardata4_bp = Blueprint('cardata4', __name__)

status = {
    "Globalclock": "",
    "Distance_to_empty": 100,
    "DistTravelled": 0,
    "DriveMode": "PARKED"
}

def check_limits(value, min_val, max_val, name):
    if value < min_val or value > max_val:
        return jsonify({"Error": f"{name} value {value} is out of range ({min_val} to {max_val})"}), 400
    return None

@cardata4_bp.route('/globalclock/get', methods=['GET'])
def globalclock_get():
    return jsonify({"Globalclock": status["Globalclock"]})

@cardata4_bp.route('/distance_to_empty/post', methods=['POST'])
def distance_to_empty_post():
    distance_to_empty = request.json["Distance_to_empty"]
    error = check_limits(distance_to_empty, 0, 100, "Distance_to_empty")
    if error:
        return error
    status["Distance_to_empty"] = distance_to_empty
    return jsonify({"Distance_to_empty": status["Distance_to_empty"]})

@cardata4_bp.route('/distance_to_empty/get', methods=['GET'])
def distance_to_empty_get():
    return jsonify({"Distance_to_empty": status["Distance_to_empty"]})

@cardata4_bp.route('/disttravelled/post', methods=['POST'])
def disttravelled_post():
    dist_travelled = request.json["DistTravelled"]
    error = check_limits(dist_travelled, 0, 1000, "DistTravelled")
    if error:
        return error
    status["DistTravelled"] = dist_travelled
    return jsonify({"DistTravelled": status["DistTravelled"]})

@cardata4_bp.route('/disttravelled/get', methods=['GET'])
def disttravelled_get():
    return jsonify({"DistTravelled": status["DistTravelled"]})

@cardata4_bp.route('/drivemode/post', methods=['POST'])
def drivemode_post():
    drive_mode = request.json["DriveMode"]
    if drive_mode not in ["PARKED", "DRIVING", "REVERSE"]:
        return jsonify({"Error": "Invalid DriveMode"}), 400
    status["DriveMode"] = drive_mode
    return jsonify({"DriveMode": status["DriveMode"]})

@cardata4_bp.route('/drivemode/get', methods=['GET'])
def drivemode_get():
    return jsonify({"DriveMode": status["DriveMode"]})

def update_globalclock():
    while True:
        status["Globalclock"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(1)