from flask import Flask, jsonify, request, Blueprint

carmode_bp = Blueprint('carmode', __name__)

car_mode = "ENTERTAINMENT_MODE"

@carmode_bp.route('/carmode/entertainment', methods=['POST'])
def entertainment_mode():
    global car_mode
    car_mode = "ENTERTAINMENT_MODE"
    return f"Car mode is now ENTERTAINMENT_MODE", 200

@carmode_bp.route('/carmode/ambient', methods=['POST'])
def ambient_mode():
    global car_mode
    car_mode = "AMBIENT_MODE"
    return f"Car mode is now AMBIENT_MODE", 200

@carmode_bp.route('/carmode/focus', methods=['POST'])
def focus_mode():
    global car_mode
    car_mode = "FOCUS_MODE"
    return f"Car mode is now FOCUS_MODE", 200

@carmode_bp.route('/carmode/night', methods=['POST'])
def night_mode():
    global car_mode
    car_mode = "NIGHT_MODE"
    return f"Car mode is now NIGHT_MODE", 200

@carmode_bp.route('/carmode/ride', methods=['POST'])
def ride_mode():
    global car_mode
    car_mode = "RIDE_MODE"
    return f"Car mode is now RIDE_MODE", 200

@carmode_bp.route('/carmode', methods=['GET'])
def get_car_mode():
    return car_mode, 200



