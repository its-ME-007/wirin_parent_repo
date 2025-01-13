# lighting_ac.py

from flask import Blueprint, jsonify, request

lighting_bp = Blueprint('lighting', __name__)

# Assuming you have a way to store the current lighting intensity
current_lighting_intensity = 0

@lighting_bp.route('/lighting/set', methods=['POST'])
def set_lighting():
    global current_lighting_intensity
    data = request.json
    intensity = data.get('intensity')
    if intensity is None:
        return jsonify({"error": "Lighting intensity is required"}), 400
    current_lighting_intensity = intensity
    result = f"Setting lighting intensity to {intensity}"
    return jsonify({"result": result})

@lighting_bp.route('/lighting/get', methods=['GET'])
def get_lighting():
    global current_lighting_intensity
    result = f"Current lighting intensity is {current_lighting_intensity}"
    return jsonify({"result": result})
