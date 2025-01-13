from flask import Flask, jsonify, request, Blueprint
import threading

#app = Flask(__name__)

int_lighting_bp = Blueprint('internal_lighting', __name__)

status = {
    "Internal": {
        "RoofLight": {"Status": 0, "Brightness": 0},
        "DoorPuddleLights": {"Status": 0, "Brightness": 0},
        "FloorLights": {"Status": 0, "Brightness": 0},
        "DashboardLights": {"Status": 0, "Brightness": 0},
        "BootLights": {"Status": 0}
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
    ]
}

@int_lighting_bp.route('/internal/rooflight/status/post', methods=['POST'])
def set_internal_rooflight_status():
    light_status = request.json["Status"]
    if light_status not in [0, 1]:
        return jsonify({"Error": "Invalid Status"}), 400
    status["Internal"]["RoofLight"]["Status"] = light_status
    return jsonify({"RoofLightStatus": status["Internal"]["RoofLight"]["Status"]})

@int_lighting_bp.route('/internal/rooflight/status/get', methods=['GET'])
def get_internal_rooflight_status():
    return jsonify({"RoofLightStatus": status["Internal"]["RoofLight"]["Status"]})

@int_lighting_bp.route('/internal/rooflight/brightness/post', methods=['POST'])
def set_internal_rooflight_brightness():
    brightness = request.json["Brightness"]
    if not 0 <= brightness <= 100:
        return jsonify({"Error": "Invalid Brightness"}), 400
    status["Internal"]["RoofLight"]["Brightness"] = brightness
    return jsonify({"RoofLightBrightness": status["Internal"]["RoofLight"]["Brightness"]})

@int_lighting_bp.route('/internal/rooflight/brightness/get', methods=['GET'])
def get_internal_rooflight_brightness():
    return jsonify({"RoofLightBrightness": status["Internal"]["RoofLight"]["Brightness"]})

@int_lighting_bp.route('/internal/doorpuddlelights/status/post', methods=['POST'])
def set_internal_doorpuddlelights_status():
    light_status = request.json["Status"]
    if light_status not in [0, 1]:
        return jsonify({"Error": "Invalid Status"}), 400
    status["Internal"]["DoorPuddleLights"]["Status"] = light_status
    return jsonify({"DoorPuddleLightsStatus": status["Internal"]["DoorPuddleLights"]["Status"]})

@int_lighting_bp.route('/internal/doorpuddlelights/status/get', methods=['GET'])
def get_internal_doorpuddlelights_status():
    return jsonify({"DoorPuddleLightsStatus": status["Internal"]["DoorPuddleLights"]["Status"]})

@int_lighting_bp.route('/internal/doorpuddlelights/brightness/post', methods=['POST'])
def set_internal_doorpuddlelights_brightness():
    brightness = request.json["Brightness"]
    if not 0 <= brightness <= 100:
        return jsonify({"Error": "Invalid Brightness"}), 400
    status["Internal"]["DoorPuddleLights"]["Brightness"] = brightness
    return jsonify({"DoorPuddleLightsBrightness": status["Internal"]["DoorPuddleLights"]["Brightness"]})

@int_lighting_bp.route('/internal/doorpuddlelights/brightness/get', methods=['GET'])
def get_internal_doorpuddlelights_brightness():
    return jsonify({"DoorPuddleLightsBrightness": status["Internal"]["DoorPuddleLights"]["Brightness"]})

# Similar functions for FloorLights
@int_lighting_bp.route('/internal/floorlights/status/post', methods=['POST'])
def set_internal_floorlights_status():
    light_status = request.json["Status"]
    if light_status not in [0, 1]:
        return jsonify({"Error": "Invalid Status"}), 400
    status["Internal"]["FloorLights"]["Status"] = light_status
    return jsonify({"FloorLightsStatus": status["Internal"]["FloorLights"]["Status"]})

@int_lighting_bp.route('/internal/floorlights/status/get', methods=['GET'])
def get_internal_floorlights_status():
    return jsonify({"FloorLightsStatus": status["Internal"]["FloorLights"]["Status"]})

@int_lighting_bp.route('/internal/floorlights/brightness/post', methods=['POST'])
def set_internal_floorlights_brightness():
    brightness = request.json["Brightness"]
    if not 0 <= brightness <= 100:
        return jsonify({"Error": "Invalid Brightness"}), 400
    status["Internal"]["FloorLights"]["Brightness"] = brightness
    return jsonify({"FloorLightsBrightness": status["Internal"]["FloorLights"]["Brightness"]})

@int_lighting_bp.route('/internal/floorlights/brightness/get', methods=['GET'])
def get_internal_floorlights_brightness():
    return jsonify({"FloorLightsBrightness": status["Internal"]["FloorLights"]["Brightness"]})

# Similar functions for DashboardLights
@int_lighting_bp.route('/internal/dashboardlights/status/post', methods=['POST'])
def set_internal_dashboardlights_status():
    light_status = request.json["Status"]
    if light_status not in [0, 1]:
        return jsonify({"Error": "Invalid Status"}), 400
    status["Internal"]["DashboardLights"]["Status"] = light_status
    return jsonify({"DashboardLightsStatus": status["Internal"]["DashboardLights"]["Status"]})

@int_lighting_bp.route('/internal/dashboardlights/status/get', methods=['GET'])
def get_internal_dashboardlights_status():
    return jsonify({"DashboardLightsStatus": status["Internal"]["DashboardLights"]["Status"]})

@int_lighting_bp.route('/internal/dashboardlights/brightness/post', methods=['POST'])
def set_internal_dashboardlights_brightness():
    brightness = request.json["Brightness"]
    if not 0 <= brightness <= 100:
        return jsonify({"Error": "Invalid Brightness"}), 400
    status["Internal"]["DashboardLights"]["Brightness"] = brightness
    return jsonify({"DashboardLightsBrightness": status["Internal"]["DashboardLights"]["Brightness"]})

@int_lighting_bp.route('/internal/dashboardlights/brightness/get', methods=['GET'])
def get_internal_dashboardlights_brightness():
    return jsonify({"DashboardLightsBrightness": status["Internal"]["DashboardLights"]["Brightness"]})

# Similar functions for BootLights
@int_lighting_bp.route('/internal/bootlights/status/post', methods=['POST'])
def set_internal_bootlights_status():
    light_status = request.json["Status"]
    if light_status not in [0, 1]:
        return jsonify({"Error": "Invalid Status"}), 400
    status["Internal"]["BootLights"]["Status"] = light_status
    return jsonify({"BootLightsStatus": status["Internal"]["BootLights"]["Status"]})

@int_lighting_bp.route('/internal/bootlights/status/get', methods=['GET'])
def get_internal_bootlights_status():
    return jsonify({"BootLightsStatus": status["Internal"]["BootLights"]["Status"]})

# Register the blueprint
# app.register_blueprint(int_lighting_bp)

# if __name__ == "__main__":
#     threading.Thread(target=internal_thread).start()
#     app.run(port=5001)
