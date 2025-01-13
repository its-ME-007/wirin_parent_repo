from flask import Flask, jsonify, request
import threading

app = Flask(__name__)

# Define the status dictionary to keep track of the states
status = {
    "Lights": {
        "Internal Lights": {
            "Roof Light": {"status": 0, "brightness": 0},
            "Door Puddle Lights": {"status": 0, "brightness": 0},
            "Floor Lights": {"status": 0, "brightness": 0},
            "Dashboard Lights": {"status": 0, "brightness": 0}
        },
        "External Lights": {
            "Boot Lights": {"status": 0, "brightness": 0},
            "Headlights": {"status": 0, "brightness": 0},
            "Tail lights": {"status": 0, "brightness": 0},
            "Brake lights": {"status": 0, "brightness": 0},
            "Turn signals": {"status": 0, "brightness": 0},
            "Fog lights": {"status": 0, "brightness": 0}
        }
    }
}

# Define endpoints for setting and getting light status
@app.route('/lights/<light_type>/<light_name>/<int:action>/<int:brightness>', methods=['POST'])
def set_light_status(light_type, light_name, action, brightness):
    """
    Set the status and brightness of a light.

    Args:
        light_type (str): The type of light (Internal Lights or External Lights).
        light_name (str): The name of the light.
        action (int): The action to perform (0 for OFF, 1 for ON).
        brightness (int): The brightness of the light (0-100).

    Returns:
        A JSON response with the updated light status.
    """
    if light_type in status["Lights"] and light_name in status["Lights"][light_type]:
        if action not in [0, 1]:
            return jsonify({"error": "Invalid action"}), 400
        if brightness < 0 or brightness > 100:
            return jsonify({"error": "Invalid brightness"}), 400
        status["Lights"][light_type][light_name]["status"] = action
        status["Lights"][light_type][light_name]["brightness"] = brightness
        return jsonify({"status": f"{light_name} is now {'ON' if action == 1 else 'OFF'} with brightness {brightness}"}), 200
    return jsonify({"error": "Invalid light type or light name"}), 400

@app.route('/lights/<light_type>/<light_name>', methods=['GET'])
def get_light_status(light_type, light_name):
    """
    Get the status of a light.

    Args:
        light_type (str): The type of light (Internal Lights or External Lights).
        light_name (str): The name of the light.

    Returns:
        A JSON response with the light status.
    """
    if light_type in status["Lights"] and light_name in status["Lights"][light_type]:
        return jsonify(status["Lights"][light_type][light_name]), 200
    return jsonify({"error": "Invalid light type or light name"}), 400

# Define endpoint for retrieving the status of all lights
@app.route('/status/lights', methods=['GET'])
def get_lights_status():
    """
    Get the status of all lights.

    Returns:
        A JSON response with the status of all lights.
    """
    return jsonify(status["Lights"]), 200

if __name__ == '__main__':
    app.run(debug=True)