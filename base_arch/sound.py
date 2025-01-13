from flask import Blueprint, jsonify, request

sound_bp = Blueprint('sound', __name__)

# Initialize the global variable
soundintensity = 0

@sound_bp.route('/sound/set', methods=['POST'])
def set_sound():
    global soundintensity
    data = request.json
    soundvolume = data.get('volume')
    if soundvolume is None:
        return jsonify({"error": "volume needs to be set"}), 400
    soundintensity = soundvolume
    result = f"Current volume is set to {soundvolume}"
    return jsonify({"result": result})

@sound_bp.route('/sound/get', methods=['GET'])
def get_sound():
    global soundintensity
    if soundintensity is None:
        return jsonify({"error": "volume is not set"}), 400
    result = f"volume is is {soundintensity}"
    return jsonify({"result": result})