from flask import Flask, jsonify, request
import threading

app = Flask(__name__)

# Define the status dictionary to keep track of the states
status = {
    "VehicleDoors": {
        "DoorStatus": "Closed",
        "BootDoorStatus": "Closed",
        "RoofDoorStatus": "Closed"
    },
    "CAR_MODE": "ENTERTAINMENT_MODE",
    "ByWireSystem": {
        "SteeringStatus": "Open",
        "AccBrakePedalStatus": "Open"
    },
    "TV": {
        "TVStateLevel": "State1",
        "TVStatus": "Moving Up"
    }
}

# Define threading functions for each component
def vehicle_doors_thread():
    @app.route('/vehicledoors/<door>/<action>', methods=['POST'])
    def vehicle_doors(door, action):
        if door in status["VehicleDoors"] and action in ["Open", "Close", "Opening", "Closing", "Error"]:
            status["VehicleDoors"][door] = action
            return jsonify({"status": f"{door} is now {action}"}), 200
        return jsonify({"error": "Invalid door or action"}), 400
    
    @app.route('/vehicledoors/<door>', methods=['GET'])
    def get_vehicle_doors(door):
        if door in status["VehicleDoors"]:
            return jsonify({door: status["VehicleDoors"][door]}), 200
        return jsonify({"error": "Invalid door"}), 400

def car_mode_thread():
    @app.route('/carmode/<mode>', methods=['POST'])
    def car_mode(mode):
        if mode in ["ENTERTAINMENT_MODE", "AMBIENT_MODE", "FOCUS_MODE", "NIGHT_MODE", "RIDE_MODE"]:
            status["CAR_MODE"] = mode
            return jsonify({"status": f"Car mode is now {mode}"}), 200
        return jsonify({"error": "Invalid mode"}), 400
    
    @app.route('/carmode', methods=['GET'])
    def get_car_mode():
        return jsonify({"CAR_MODE": status["CAR_MODE"]}), 200

def by_wire_system_thread():
    @app.route('/bywiresystem/<component>/<action>', methods=['POST'])
    def by_wire_system(component, action):
        if component in status["ByWireSystem"] and action in ["Open", "Close", "Opening", "Closing", "Error"]:
            status["ByWireSystem"][component] = action
            return jsonify({"status": f"{component} is now {action}"}), 200
        return jsonify({"error": "Invalid component or action"}), 400
    
    @app.route('/bywiresystem/<component>', methods=['GET'])
    def get_by_wire_system(component):
        if component in status["ByWireSystem"]:
            return jsonify({component: status["ByWireSystem"][component]}), 200
        return jsonify({"error": "Invalid component"}), 400

def tv_thread():
    @app.route('/tv/statelevel/<level>', methods=['POST'])
    def tv_state_level(level):
        if level in ["State1", "State2", "State3"]:
            status["TV"]["TVStateLevel"] = level
            return jsonify({"status": f"TV state level is now {level}"}), 200
        return jsonify({"error": "Invalid state level"}), 400
    
    @app.route('/tv/statelevel', methods=['GET'])
    def get_tv_state_level():
        return jsonify({"TVStateLevel": status["TV"]["TVStateLevel"]}), 200

    @app.route('/tv/status/<state>', methods=['POST'])
    def tv_status(state):
        if state in ["Moving Up", "Moving Down", "State1", "State2", "State3", "Error"]:
            status["TV"]["TVStatus"] = state
            return jsonify({"status": f"TV status is now {state}"}), 200
        return jsonify({"error": "Invalid TV status"}), 400
    
    @app.route('/tv/status', methods=['GET'])
    def get_tv_status():
        return jsonify({"TVStatus": status["TV"]["TVStatus"]}), 200

# Define endpoints for retrieving the status of each component
@app.route('/status/vehicledoors', methods=['GET'])
def get_vehicle_doors_status():
    return jsonify(status["VehicleDoors"]), 200

@app.route('/status/carmode', methods=['GET'])
def get_car_mode_status():
    return jsonify({"CAR_MODE": status["CAR_MODE"]}), 200

@app.route('/status/bywiresystem', methods=['GET'])
def get_by_wire_system_status():
    return jsonify(status["ByWireSystem"]), 200

@app.route('/status/tv', methods=['GET'])
def get_tv_status():
    return jsonify(status["TV"]), 200

# Start the threads
threads = []
threads.append(threading.Thread(target=vehicle_doors_thread))
threads.append(threading.Thread(target=car_mode_thread))
threads.append(threading.Thread(target=by_wire_system_thread))
threads.append(threading.Thread(target=tv_thread))

for thread in threads:
    thread.start()

if __name__ == '__main__':
    app.run(debug=True)