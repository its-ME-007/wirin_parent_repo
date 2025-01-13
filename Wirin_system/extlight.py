from flask import Flask, jsonify, request, Blueprint

ext_lighting_bp = Blueprint('external_lighting', __name__)

status = {
    "External": {
        "Headlights": {"Status": 0},
        "TailLights": {"Status": 0},
        "BrakeLights": {"Status": 0},
        "TurnSignals": {"Status": 0},
        "FogLights": {"Status": 0}
    }
}

endpoints = {
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
    ]
}

@ext_lighting_bp.route('/external/headlights/status/post', methods=['POST'])
def set_external_headlights_status():
    light_status = request.json["Status"]
    if light_status not in [0, 1]:
        return jsonify({"Error": "Invalid Status"}), 400
    status["External"]["Headlights"]["Status"] = light_status
    return jsonify({"HeadlightsStatus": status["External"]["Headlights"]["Status"]})

@ext_lighting_bp.route('/external/headlights/status/get', methods=['GET'])
def get_external_headlights_status():
    return jsonify({"HeadlightsStatus": status["External"]["Headlights"]["Status"]})

@ext_lighting_bp.route('/external/taillights/status/post', methods=['POST'])
def set_external_taillights_status():
    light_status = request.json["Status"]
    if light_status not in [0, 1]:
        return jsonify({"Error": "Invalid Status"}), 400
    status["External"]["TailLights"]["Status"] = light_status
    return jsonify({"TailLightsStatus": status["External"]["TailLights"]["Status"]})

@ext_lighting_bp.route('/external/taillights/status/get', methods=['GET'])
def get_external_taillights_status():
    return jsonify({"TailLightsStatus": status["External"]["TailLights"]["Status"]})

@ext_lighting_bp.route('/external/brakelights/status/post', methods=['POST'])
def set_external_brakelights_status():
    light_status = request.json["Status"]
    if light_status not in [0, 1]:
        return jsonify({"Error": "Invalid Status"}), 400
    status["External"]["BrakeLights"]["Status"] = light_status
    return jsonify({"BrakeLightsStatus": status["External"]["BrakeLights"]["Status"]})

@ext_lighting_bp.route('/external/brakelights/status/get', methods=['GET'])
def get_external_brakelights_status():
    return jsonify({"BrakeLightsStatus": status["External"]["BrakeLights"]["Status"]})

@ext_lighting_bp.route('/external/turnsignals/status/post', methods=['POST'])
def set_external_turnsignals_status():
    light_status = request.json["Status"]
    if light_status not in [0, 1]:
        return jsonify({"Error": "Invalid Status"}), 400
    status["External"]["TurnSignals"]["Status"] = light_status
    return jsonify({"TurnSignalsStatus": status["External"]["TurnSignals"]["Status"]})

@ext_lighting_bp.route('/external/turnsignals/status/get', methods=['GET'])
def get_external_turnsignals_status():
    return jsonify({"TurnSignalsStatus": status["External"]["TurnSignals"]["Status"]})

@ext_lighting_bp.route('/external/foglights/status/post', methods=['POST'])
def set_external_foglights_status():
    light_status = request.json["Status"]
    if light_status not in [0, 1]:
        return jsonify({"Error": "Invalid Status"}), 400
    status["External"]["FogLights"]["Status"] = light_status
    return jsonify({"FogLightsStatus": status["External"]["FogLights"]["Status"]})

@ext_lighting_bp.route('/external/foglights/status/get', methods=['GET'])
def get_external_foglights_status():
    return jsonify({"FogLightsStatus": status["External"]["FogLights"]["Status"]})
