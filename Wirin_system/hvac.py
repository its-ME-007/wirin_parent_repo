
from flask import Flask, jsonify, request, Blueprint
import threading

hvac_bp = Blueprint('hvac', __name__)


# Define the status dictionary to keep track of the states
status = {
    "HVAC": {
        "Temperature": 0,
        "FanSpeed": 0,
        "ACStatus": 0,
        "ACBlowToSeatFrontRight": 0,
        "ACBlowToSeatFrontLeft": 0,
        "ACBlowToSeatRearRight": 0,
        "ACBlowToSeatRearLeft": 0
    }
}

# Define a lock for thread safety
lock = threading.Lock()

# Define a function to validate the component
def validate_component(component):
    if not isinstance(component, str):
        return False
    return component in status["HVAC"]

# Define a function to validate the value
def validate_value(component, value):
    if not isinstance(value, int):
        return False
    if component == "Temperature" and 0 <= value <= 100:
        return True
    elif component == "FanSpeed" and 0 <= value <= 100:
        return True
    elif component == "ACStatus" and value in (0, 1):
        return True
    elif component in ("ACBlowToSeatFrontRight", "ACBlowToSeatFrontLeft", "ACBlowToSeatRearRight", "ACBlowToSeatRearLeft") and value in (0, 1):
        return True
    return False

# Define endpoints for setting the value of each component

@hvac_bp.route('/hvac/<component>/<int:value>', methods=['POST'])

def set_hvac_value(component, value):
    with lock:
        try:
            if validate_component(component) and validate_value(component, value):
                status["HVAC"][component] = value
                return jsonify({"status": f"{component} is now {value}"}), 200
            else:
                return jsonify({"error": "Invalid component or value"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

# Define endpoints for retrieving the value of each component

@hvac_bp.route('/hvac/<component>', methods=['GET'])

def get_hvac_value(component):
    with lock:
        try:
            if validate_component(component):
                return jsonify({component: status["HVAC"][component]}), 200
            else:
                return jsonify({"error": "Invalid component"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

# Define endpoints for retrieving the status of each component

@hvac_bp.route('/status/hvac', methods=['GET'])

def get_hvac_status():
    with lock:
        try:
            return jsonify(status["HVAC"]), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
