from flask import Blueprint, jsonify, request,Flask
ac_bp = Blueprint('ac', __name__)

# Initialize the global variable
current_ac = 0

@ac_bp.route('/ac/set', methods=['POST'])
def set_ac():
    global current_ac
    data = request.json
    actemperature = data.get('temperature')
    if actemperature is None:
        return jsonify({"error": "ac temperature is required"}), 400
    current_ac = actemperature
    result = f"Current ac temperature is set to {actemperature}"
    return jsonify({"result": result})

@ac_bp.route('/ac/get', methods=['GET'])
def get_ac():
    global current_ac
    if current_ac is None:
        return jsonify({"error": "ac temperature is not set"}), 400
    result = f"Current ac temperature is {current_ac}"
    return jsonify({"result": result})








