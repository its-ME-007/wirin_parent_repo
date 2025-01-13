from flask import Blueprint, jsonify, request

cardata1_bp = Blueprint('cardata1', __name__)

status = {
    "SpeedL": 0,
    "SpeedR": 0,
    "SteeringAngle": 0,
    "BrakeLevel": 0,
    "Gear": "Neutral",
    "FootSwitch": "ON",
    "MotorBrake": "ON",
    "KellyLStatus": 0,
    "KellyRStatus": 0,
    "VehicleError": 0,
}

def check_limits(value, min_val, max_val, name):
    if value < min_val or value > max_val:
        return jsonify({"Error": f"{name} value {value} is out of range ({min_val} to {max_val})"}), 400
    return None

@cardata1_bp.route('/speed/<side>/post', methods=['POST'])
def speed_post(side):
    speed = request.json["Speed"]
    error = check_limits(speed, 0, 5000, "Speed")
    if error:
        return error
    if side == "L":
        status["SpeedL"] = speed
    elif side == "R":
        status["SpeedR"] = speed
    else:
        return jsonify({"Error": "Invalid side"}), 400
    return jsonify({"Speed": status[f"Speed{side}"]})

@cardata1_bp.route('/speed/<side>/get', methods=['GET'])
def speed_get(side):
    if side == "L":
        return jsonify({"Speed": status["SpeedL"]})
    elif side == "R":
        return jsonify({"Speed": status["SpeedR"]})
    else:
        return jsonify({"Error": "Invalid side"}), 400

@cardata1_bp.route('/steeringangle/post', methods=['POST'])
def steeringangle_post():
    steering_angle = request.json["SteeringAngle"]
    error = check_limits(steering_angle, -30, 30, "SteeringAngle")
    if error:
        return error
    status["SteeringAngle"] = steering_angle
    return jsonify({"SteeringAngle": status["SteeringAngle"]})

@cardata1_bp.route('/steeringangle/get', methods=['GET'])
def steeringangle_get():
    return jsonify({"SteeringAngle": status["SteeringAngle"]})

@cardata1_bp.route('/brakelevel/post', methods=['POST'])
def brakelevel_post():
    brake_level = request.json["BrakeLevel"]
    error = check_limits(brake_level, 0, 100, "BrakeLevel")
    if error:
        return error
    status["BrakeLevel"] = brake_level
    return jsonify({"BrakeLevel": status["BrakeLevel"]})
    
@cardata1_bp.route('/brakelevel/get', methods=['GET'])
def brakelevel_get():
    return jsonify({"BrakeLevel": status["BrakeLevel"]})
