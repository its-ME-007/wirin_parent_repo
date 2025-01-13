from flask import Blueprint, jsonify, request

tv_bp = Blueprint('tv', __name__)

# Assuming you have a way to store the current TV state
tv_state_level = "State1"
tv_status = "Moving Up"

@tv_bp.route('/tv/statelevel/set', methods=['POST'])
def set_tv_state_level():
    global tv_state_level
    data = request.json
    level = data.get('level')
    if level not in ["State1", "State2", "State3"]:
        return jsonify({"error": "Invalid state level"}), 400
    tv_state_level = level
    result = f"Setting TV state level to {level}"
    return jsonify({"result": result})

@tv_bp.route('/tv/statelevel/get', methods=['GET'])
def get_tv_state_level():
    global tv_state_level
    result = f"Current TV state level is {tv_state_level}"
    return jsonify({"result": result})

@tv_bp.route('/tv/status/set', methods=['POST'])
def set_tv_status():
    global tv_status
    data = request.json
    state = data.get('state')
    if state not in ["Moving Up", "Moving Down", "State1", "State2", "State3", "Error"]:
        return jsonify({"error": "Invalid TV status"}), 400
    tv_status = state
    result = f"Setting TV status to {state}"
    return jsonify({"result": result})

@tv_bp.route('/tv/status/get', methods=['GET'])
def get_tv_status():
    global tv_status
    result = f"Current TV status is {tv_status}"
    return jsonify({"result": result})
