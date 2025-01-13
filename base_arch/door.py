from flask import Blueprint,Flask, jsonify, request

door_bp = Blueprint('door', __name__)

# Initialize the door statuses (False means closed, True means open)
doors = {
    'door1': True,
    'door2': True,
    'door3': True,
    'door4': True
}

@door_bp.route('/door/<door_id>/status', methods=['POST'])
def update_door_status(door_id):
    if door_id not in doors:
        return jsonify({"error": "Invalid door ID"}), 400

    data = request.json
    status = data.get('status')
    if status is None or not isinstance(status, bool):
        return jsonify({"error": "Invalid status, must be a boolean"}), 400

    doors[door_id] = status
    return jsonify({"message": f"Status of {door_id} updated to {'open' if status else 'closed'}"})

@door_bp.route('/car/can_start', methods=['GET'])
def can_car_start():
    # Check if all doors are closed
    if all(not status for status in doors.values()):
        return jsonify({"car_can_start": 1})
    else:
        return jsonify({"car_can_start": 0})

