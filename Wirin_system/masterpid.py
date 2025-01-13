from flask import Blueprint, jsonify, request

master_pid_values_bp = Blueprint('master_pid_values', __name__)

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

@master_pid_values_bp.route('/controlsettings/masterpidvalues/<component>/<int:value>', methods=['POST'])
def set_master_pid_values(component, value):
    if component in status["ControlSettings"]["MasterPIDValues"]:
        if component in ["SteeringPIDOutput", "BrakePIDOutput"]:
            if -1024 <= value <= 1024:
                status["ControlSettings"]["MasterPIDValues"][component] = value
                return jsonify({"status": f"{component} is now {value}"}), 200
        elif component in ["MotorRPIDOutput", "MotorLPIDOutput"]:
            if 0 <= value <= 5000:
                status["ControlSettings"]["MasterPIDValues"][component] = value
                return jsonify({"status": f"{component} is now {value}"}), 200
        elif component == "MasterPIDCommandOutput":
            if 0 <= value <= 1000:
                status["ControlSettings"]["MasterPIDValues"][component] = value
                return jsonify({"status": f"{component} is now {value}"}), 200
    return jsonify({"error": "Invalid component or value"}), 400

@master_pid_values_bp.route('/controlsettings/masterpidvalues/<component>', methods=['GET'])
def get_master_pid_values(component):
    if component in status["ControlSettings"]["MasterPIDValues"]:
        return jsonify({component: status["ControlSettings"]["MasterPIDValues"][component]}), 200
    return jsonify({"error": "Invalid component"}), 400
