from flask import Blueprint, jsonify, request

pid_status_bp = Blueprint('pid_status', __name__)

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

@pid_status_bp.route('/controlsettings/pidstatus/<component>/<action>', methods=['POST'])
def set_pid_status(component, action):
    if component in status["ControlSettings"]["PIDStatus"] and action in ["ON", "OFF"]:
        status["ControlSettings"]["PIDStatus"][component] = action
        return jsonify({"status": f"{component} is now {action}"}), 200
    return jsonify({"error": "Invalid component or action"}), 400

@pid_status_bp.route('/controlsettings/pidstatus/<component>', methods=['GET'])
def get_pid_status(component):
    if component in status["ControlSettings"]["PIDStatus"]:
        return jsonify({component: status["ControlSettings"]["PIDStatus"][component]}), 200
    return jsonify({"error": "Invalid component"}), 400
