from flask import Flask, jsonify, request
import threading
from datetime import datetime
import time

app = Flask(__name__)

status = {
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
    }
}

# Error handling functions
def check_limits(value, min_val, max_val, name):
    if value < min_val or value > max_val:
        return jsonify({"Error": f"{name} value {value} is out of range ({min_val} to {max_val})"}), 400
    return None

# Define cardata1 thread routes
def cardata1_thread():
    @app.route('/cardata/cardata1/speed/<side>/post', methods=['POST'])
    def cardata1_speed(side):
        speed = request.json["Speed"]
        error = check_limits(speed, 0, 5000, "Speed")
        if error:
            return error
        if side == "L":
            status["CarData"]["cardata1"]["SpeedL"] = speed
        elif side == "R":
            status["CarData"]["cardata1"]["SpeedR"] = speed
        else:
            return jsonify({"Error": "Invalid side"}), 400
        return jsonify({"Speed": status["CarData"]["cardata1"][f"Speed{side}"]})

    @app.route('/cardata/cardata1/speed/<side>/get', methods=['GET'])
    def cardata1_speed_get(side):
        if side == "L":
            return jsonify({"Speed": status["CarData"]["cardata1"]["SpeedL"]})
        elif side == "R":
            return jsonify({"Speed": status["CarData"]["cardata1"]["SpeedR"]})
        else:
            return jsonify({"Error": "Invalid side"}), 400

    @app.route('/cardata/cardata1/steeringangle/post', methods=['POST'])
    def cardata1_steeringangle():
        steering_angle = request.json["SteeringAngle"]
        error = check_limits(steering_angle, -30, 30, "SteeringAngle")
        if error:
            return error
        status["CarData"]["cardata1"]["SteeringAngle"] = steering_angle
        return jsonify({"SteeringAngle": status["CarData"]["cardata1"]["SteeringAngle"]})

    @app.route('/cardata/cardata1/steeringangle/get', methods=['GET'])
    def cardata1_steeringangle_get():
        return jsonify({"SteeringAngle": status["CarData"]["cardata1"]["SteeringAngle"]})

    @app.route('/cardata/cardata1/brakelevel/post', methods=['POST'])
    def cardata1_brakelevel():
        brake_level = request.json["BrakeLevel"]
        error = check_limits(brake_level, 0, 100, "BrakeLevel")
        if error:
            return error
        status["CarData"]["cardata1"]["BrakeLevel"] = brake_level
        return jsonify({"BrakeLevel": status["CarData"]["cardata1"]["BrakeLevel"]})

    @app.route('/cardata/cardata1/brakelevel/get', methods=['GET'])
    def cardata1_brakelevel_get():
        return jsonify({"BrakeLevel": status["CarData"]["cardata1"]["BrakeLevel"]})

    # Similarly define other routes for cardata1 fields...

# Define cardata2 thread routes
def cardata2_thread():
    @app.route('/cardata/cardata2/ihumidity/post', methods=['POST'])
    def cardata2_ihumidity():
        ihumidity = request.json["ihumidity"]
        error = check_limits(ihumidity, 0, 100, "ihumidity")
        if error:
            return error
        status["CarData"]["cardata2"]["ihumidity"] = ihumidity
        return jsonify({"ihumidity": status["CarData"]["cardata2"]["ihumidity"]})

    @app.route('/cardata/cardata2/ihumidity/get', methods=['GET'])
    def cardata2_ihumidity_get():
        return jsonify({"ihumidity": status["CarData"]["cardata2"]["ihumidity"]})

    @app.route('/cardata/cardata2/itemperature/post', methods=['POST'])
    def cardata2_itemperature():
        itemperature = request.json["itemperature"]
        error = check_limits(itemperature, 0, 100, "itemperature")
        if error:
            return error
        status["CarData"]["cardata2"]["itemperature"] = itemperature
        return jsonify({"itemperature": status["CarData"]["cardata2"]["itemperature"]})

    @app.route('/cardata/cardata2/itemperature/get', methods=['GET'])
    def cardata2_itemperature_get():
        return jsonify({"itemperature": status["CarData"]["cardata2"]["itemperature"]})

# Define cardata3 thread routes
def cardata3_thread():
    @app.route('/cardata/cardata3/can/<num>/stat/post', methods=['POST'])
    def cardata3_can_stat(num):
        if num in ["1", "2", "3"]:
            status["CarData"]["cardata3"][f"CAN{num}Stat"] = request.json["Status"]
            return jsonify({f"CAN{num}Stat": status["CarData"]["cardata3"][f"CAN{num}Stat"]})
        else:
            return jsonify({"Error": "Invalid CAN number"}), 400

    @app.route('/cardata/cardata3/can/<num>/stat/get', methods=['GET'])
    def cardata3_can_stat_get(num):
        if num in ["1", "2", "3"]:
            return jsonify({f"CAN{num}Stat": status["CarData"]["cardata3"][f"CAN{num}Stat"]})
        else:
            return jsonify({"Error": "Invalid CAN number"}), 400

    @app.route('/cardata/cardata3/internet/post', methods=['POST'])
    def cardata3_internet():
        status["CarData"]["cardata3"]["Internet"] = request.json["Internet"]
        return jsonify({"Internet": status["CarData"]["cardata3"]["Internet"]})

    @app.route('/cardata/cardata3/internet/get', methods=['GET'])
    def cardata3_internet_get():
        return jsonify({"Internet": status["CarData"]["cardata3"]["Internet"]})

    @app.route('/cardata/cardata3/ethernet/post', methods=['POST'])
    def cardata3_ethernet():
        status["CarData"]["cardata3"]["Ethernet"] = request.json["Ethernet"]
        return jsonify({"Ethernet": status["CarData"]["cardata3"]["Ethernet"]})

    @app.route('/cardata/cardata3/ethernet/get', methods=['GET'])
    def cardata3_ethernet_get():
        return jsonify({"Ethernet": status["CarData"]["cardata3"]["Ethernet"]})

# Define cardata4 thread routes
def cardata4_thread():
    @app.route('/cardata/cardata4/globalclock/get', methods=['GET'])
    def cardata4_globalclock_get():
        return jsonify({"Globalclock": status["CarData"]["cardata4"]["Globalclock"]})

    @app.route('/cardata/cardata4/distance_to_empty/post', methods=['POST'])
    def cardata4_distance_to_empty():
        distance_to_empty = request.json["Distance_to_empty"]
        error = check_limits(distance_to_empty, 0, 100, "Distance_to_empty")
        if error:
            return error
        status["CarData"]["cardata4"]["Distance_to_empty"] = distance_to_empty
        return jsonify({"Distance_to_empty": status["CarData"]["cardata4"]["Distance_to_empty"]})

    @app.route('/cardata/cardata4/distance_to_empty/get', methods=['GET'])
    def cardata4_distance_to_empty_get():
        return jsonify({"Distance_to_empty": status["CarData"]["cardata4"]["Distance_to_empty"]})

    @app.route('/cardata/cardata4/disttravelled/post', methods=['POST'])
    def cardata4_disttravelled():
        dist_travelled = request.json["DistTravelled"]
        error = check_limits(dist_travelled, 0, 1000, "DistTravelled")
        if error:
            return error
        status["CarData"]["cardata4"]["DistTravelled"] = dist_travelled
        return jsonify({"DistTravelled": status["CarData"]["cardata4"]["DistTravelled"]})

    @app.route('/cardata/cardata4/disttravelled/get', methods=['GET'])
    def cardata4_disttravelled_get():
        return jsonify({"DistTravelled": status["CarData"]["cardata4"]["DistTravelled"]})

    @app.route('/cardata/cardata4/drivemode/post', methods=['POST'])
    def cardata4_drivemode():
        drive_mode = request.json["DriveMode"]
        if drive_mode not in ["PARKED", "DRIVING", "REVERSE"]:
            return jsonify({"Error": "Invalid DriveMode"}), 400
        status["CarData"]["cardata4"]["DriveMode"] = drive_mode
        return jsonify({"DriveMode": status["CarData"]["cardata4"]["DriveMode"]})

    @app.route('/cardata/cardata4/drivemode/get', methods=['GET'])
    def cardata4_drivemode_get():
        return jsonify({"DriveMode": status["CarData"]["cardata4"]["DriveMode"]})

# Define the function to update the global clock
def update_globalclock():
    while True:
        status["CarData"]["cardata4"]["Globalclock"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(1)

# Start threads
if __name__ == '__main__':
    threading.Thread(target=cardata1_thread).start()
    threading.Thread(target=cardata2_thread).start()
    threading.Thread(target=cardata3_thread).start()
    threading.Thread(target=cardata4_thread).start()
    threading.Thread(target=update_globalclock).start()
    app.run(debug=True)
