from flask import request, jsonify, Blueprint
import os

vol_bp = Blueprint('sound', __name__)

@vol_bp.route('/volume/set', methods=['POST'])
def set_volume():
    data = request.json
    volume = data.get('volume')
    global current_vol
    current_vol = volume
    if not isinstance(volume, int) or not (0 <= volume <= 100):
        return jsonify({"status": "error", "result": "Volume must be an integer between 0 and 100"}), 400
    try:
        os.system(f"amixer set Master {volume}%")
        result = f"Setting speaker volume to {volume}"
        return jsonify({"status": "success", "result": result})
    except Exception as e:
        return jsonify({"status": "error", "result": str(e)}), 500
    
@vol_bp.route('/volume/get', methods=['GET'])
def get_volume():
    result = f"Current volume is {current_vol}"
    return jsonify({"result": result})

@vol_bp.route('/volume/mute', methods=['POST'])
def mute():
    try:
        os.system("amixer set Master 0")
        result = "Speaker muted"
        return jsonify({"status": "success", "result": result})
    except Exception as e:
        return jsonify({"status": "error", "result": str(e)}), 500

@vol_bp.route('/volume/unmute', methods=['POST'])
def unmute():
    data = request.json
    volume = data.get('volume')
    global current_vol
    current_vol = volume
    if not isinstance(volume, int) or not (0 <= volume <= 100):
        return jsonify({"status": "error", "result": "Volume must be an integer between 0 and 100"}), 400
    try:
        os.system(f"amixer set Master {volume}%")
        result = f"Setting speaker volume to {volume}"
        return jsonify({"status": "success", "result": result})
    except Exception as e:
        return jsonify({"status": "error", "result": str(e)}), 500

