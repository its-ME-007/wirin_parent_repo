from flask import Flask, jsonify, request
import threading
from datetime import datetime
import time
from flask import Blueprint

#app = Flask(__name__)

obc_bp = Blueprint('obc', __name__)

status = {
    "Lighting": {
        "Internal": {
            "RoofLight": {"Status": 0, "Brightness": 0},
            "DoorPuddleLights": {"Status": 0, "Brightness": 0},
            "FloorLights": {"Status": 0, "Brightness": 0},
            "DashboardLights": {"Status": 0, "Brightness": 0},
            "BootLights": {"Status": 0}
        },
        "External": {
            "Headlights": {"Status": 0},
            "TailLights": {"Status": 0},
            "BrakeLights": {"Status": 0},
            "TurnSignals": {"Status": 0},
            "FogLights": {"Status": 0}
        }
    },
    "CarData": {
        "cardata1": {
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
        },
        "cardata2": {
            "ihumidity": 0,
            "itemperature": 0,
        },
        "cardata3": {
            "CAN1Stat": "Active",
            "CAN2Stat": "Active",
            "CAN3Stat": "Active",
            "Internet": "Active",
            "Ethernet": "Active"
        },
        "cardata4": {
            "Globalclock": "",
            "Distance_to_empty": 100,
            "DistTravelled": 0,
            "DriveMode": "PARKED"
        }
    },
    "OBC": {
        "AC_Voltage": 0,
        "AC_Current": 0,
        "AC_Power": 0,
        "Charging_Time": 0,
        "DC_Voltage": 0,
        "DC_Current": 0,
        "OBC_Temperature": 0,
        "OBC_Status": 0
    }
}

endpoints = {
    "internal_lighting_endpoints": [
        "/internal/rooflight/status/post",
        "/internal/rooflight/brightness/post",
        "/internal/doorpuddlelights/status/post",
        "/internal/doorpuddlelights/brightness/post",
        "/internal/floorlights/status/post",
        "/internal/floorlights/brightness/post",
        "/internal/dashboardlights/status/post",
        "/internal/dashboardlights/brightness/post",
        "/internal/bootlights/status/post",
        "/internal/rooflight/status/get",
        "/internal/rooflight/brightness/get",
        "/internal/doorpuddlelights/status/get",
        "/internal/doorpuddlelights/brightness/get",
        "/internal/floorlights/status/get",
        "/internal/floorlights/brightness/get",
        "/internal/dashboardlights/status/get",
        "/internal/dashboardlights/brightness/get",
        "/internal/bootlights/status/get"
    ],
    "external_lighting_endpoints": [
        "/external/headlights/status/post",
        "/external/taillights/status/post",
        "/external/brakelights/status/post",
        "/external/turnsignals/status/post",
        "/external/foglights/status/post",
        "/external/headlights/status/get",
        "/external/taillights/status/get",
        "/external/brakelights/status/get",
        "/external/turnsignals/status/get",
        "/external/foglights/status/get"
    ],
    "obc_endpoints": [
        "/obc/ac_voltage/get",
        "/obc/ac_current/get",
        "/obc/ac_power/get",
        "/obc/charging_time/get",
        "/obc/dc_voltage/get",
        "/obc/dc_current/get",
        "/obc/obc_temperature/get",
        "/obc/obc_status/get"
    ]
}


@obc_bp.route('/obc/ac_voltage/get', methods=['GET'])
def get_ac_voltage():
    return jsonify({"AC_Voltage": status["OBC"]["AC_Voltage"]})

@obc_bp.route('/obc/ac_current/get', methods=['GET'])
def get_ac_current():
    return jsonify({"AC_Current": status["OBC"]["AC_Current"]})

@obc_bp.route('/obc/ac_power/get', methods=['GET'])
def get_ac_power():
    return jsonify({"AC_Power": status["OBC"]["AC_Power"]})

@obc_bp.route('/obc/charging_time/get', methods=['GET'])
def get_charging_time():
    return jsonify({"Charging_Time": status["OBC"]["Charging_Time"]})

@obc_bp.route('/obc/dc_voltage/get', methods=['GET'])
def get_dc_voltage():
    return jsonify({"DC_Voltage": status["OBC"]["DC_Voltage"]})

@obc_bp.route('/obc/dc_current/get', methods=['GET'])
def get_dc_current():
    return jsonify({"DC_Current": status["OBC"]["DC_Current"]})

@obc_bp.route('/obc/obc_temperature/get', methods=['GET'])
def get_obc_temperature():
    return jsonify({"OBC_Temperature": status["OBC"]["OBC_Temperature"]})

@obc_bp.route('/obc/obc_status/get', methods=['GET'])
def get_obc_status():
    return jsonify({"OBC_Status": status["OBC"]["OBC_Status"]})
=======

app = Flask(__name__)

# Define the status dictionary to keep track of the states
status = {
    "OBC": {
        "ACVoltage": 0,
        "ACCurrent": 0,
        "ACPower": 0,
        "ChargingTime": 0,
        "DCVoltage": 0,
        "DCCurrent": 0,
        "OBCTemperature": 0,
        "OBCStatus": 0
    }
}

# Define a lock for thread safety
lock = threading.Lock()

# Define endpoints for setting the value of each component
@app.route('/obc/<component>/<int:value>', methods=['POST'])
def set_obc_value(component, value):
    with lock:
        if component in status["OBC"]:
            if component == "ACVoltage" and 0 <= value <= 300:
                status["OBC"][component] = value
                return jsonify({"status": f"{component} is now {value}"}), 200
            elif component == "ACCurrent" and 0 <= value <= 100:
                status["OBC"][component] = value
                return jsonify({"status": f"{component} is now {value}"}), 200
            elif component == "ACPower" and 0 <= value <= 4000:
                status["OBC"][component] = value
                return jsonify({"status": f"{component} is now {value}"}), 200
            elif component == "ChargingTime" and 0 <= value <= 999:
                status["OBC"][component] = value
                return jsonify({"status": f"{component} is now {value}"}), 200
            elif component == "DCVoltage" and 0 <= value <= 100:
                status["OBC"][component] = value
                return jsonify({"status": f"{component} is now {value}"}), 200
            elif component == "DCCurrent" and 0 <= value <= 100:
                status["OBC"][component] = value
                return jsonify({"status": f"{component} is now {value}"}), 200
            elif component == "OBCTemperature" and 0 <= value <= 150:
                status["OBC"][component] = value
                return jsonify({"status": f"{component} is now {value}"}), 200
            elif component == "OBCStatus" and 0 <= value <= 255:
                status["OBC"][component] = value
                return jsonify({"status": f"{component} is now {value}"}), 200
        return jsonify({"error": "Invalid component or value"}), 400

# Define endpoints for retrieving the value of each component
@app.route('/obc/<component>', methods=['GET'])
def get_obc_value(component):
    with lock:
        if component in status["OBC"]:
            return jsonify({component: status["OBC"][component]}), 200
        return jsonify({"error": "Invalid component"}), 400

# Define endpoints for retrieving the status of each component
@app.route('/status/obc', methods=['GET'])
def get_obc_status():
    with lock:
        return jsonify(status["OBC"]), 200

if __name__ == '__main__':
    app.run(debug=True)

