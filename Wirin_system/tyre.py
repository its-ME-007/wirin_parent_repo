from flask import Flask, jsonify, request

from flask import Blueprint
tyre_bp = Blueprint('tyre', __name__)

status = {
    "TyrePressure": {
        "front_right_wheel": 0,
        "front_left_wheel": 0,
        "rear_right_wheel": 0,
        "rear_left_wheel": 0
    }
}

def check_limits(value, min_val, max_val, name):
    if value < min_val or value > max_val:
        return jsonify({"Error": f"{name} value {value} is out of range ({min_val} to {max_val})"}), 400
    return None

def tyre_pressure_thread():

    @tyre_bp.route('/Tyrepressure/<point>/<side>/get', methods=['GET'])

    def tyre_pressure_get(point, side):
        if point == 'F':
            if side == "L":
                pressure = status["TyrePressure"]["front_left_wheel"]
            elif side == "R":
                pressure = status["TyrePressure"]["front_right_wheel"]
            else:
                return jsonify({"Error": "Invalid side"}), 400
        elif point == 'B':
            if side == "L":
                pressure = status["TyrePressure"]["rear_left_wheel"]
            elif side == "R":
                pressure = status["TyrePressure"]["rear_right_wheel"]
            else:
                return jsonify({"Error": "Invalid side"}), 400
        else:
            return jsonify({"Error": "Invalid point"}), 400
        return jsonify({"Pressure": pressure}), 200


    @tyre_bp.route('/Tyrepressure/all/get', methods=['GET'])

    def tyre_pressure_get_all():
        return jsonify(status["TyrePressure"]), 200

# Start the tyre pressure thread
tyre_pressure_thread()

