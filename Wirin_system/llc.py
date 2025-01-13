from flask import Blueprint, jsonify, request

control_settings_bp = Blueprint('lowlevelcontrol', __name__)

# Define the status dictionary to keep track of the states
status = {
    "ControlSettings": {
        "LowLevelControlMode": "Manual Mode",
        "PIDStatus": {
            "MasterControl": "OFF",
            "SteeringRack": "OFF",
            "Brake": "OFF",
            "Motors": "OFF"
        },
        "MasterPIDValues": {
            "SteeringPIDOutput": 0,
            "BrakePIDOutput": 0,
            "MotorRPIDOutput": 0,
            "MotorLPIDOutput": 0,
            "MasterPIDCommandOutput": 0
        }
    }
}

@control_settings_bp.route('/controlsettings/lowlevelcontrolmode/<mode>', methods=['POST'])
def set_low_level_control_mode(mode):
    if mode in ["Autonomous LEVEL 5", "Autonomous LEVEL 4", "Autonomous LEVEL 3", "Autonomous LEVEL 2", "Autonomous LEVEL 1", "Manual Mode", "Hardware Mode"]:
        status["ControlSettings"]["LowLevelControlMode"] = mode
        return jsonify({"status": f"Low Level Control Mode is now {mode}"}), 200
    return jsonify({"error": "Invalid mode"}), 400

@control_settings_bp.route('/controlsettings/lowlevelcontrolmode', methods=['GET'])
def get_low_level_control_mode():
    return jsonify({"LowLevelControlMode": status["ControlSettings"]["LowLevelControlMode"]}), 200
