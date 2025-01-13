from flask import Flask, jsonify, request, Blueprint
import threading

seat_bp = Blueprint('seat_bp', __name__)

# Define the status dictionary to keep track of the states
status = {
    "Seat": {
        "CaptainSeat": {
            "FacingPosition": "Front",
            "BackrestPosition": 0
        },
        "CoCaptainSeat": {
            "FacingPosition": "Front",
            "BackrestPosition": 0
        }
    }
}



# Define threading functions for each seat component
@seat_bp.route('/seat/captain/facingposition/<string:position>', methods=['POST'])
def set_captain_seat_facing_position(position):
    if position in ["Front", "Side", "Back", "Rotating"]:
        status["Seat"]["CaptainSeat"]["FacingPosition"] = position
        return jsonify({"status": f"Captain seat facing position is now {position}"}), 200
    return jsonify({"error": "Invalid facing position value"}), 400

@seat_bp.route('/seat/captain/facingposition', methods=['GET'])
def get_captain_seat_facing_position():
    return jsonify({"FacingPosition": status["Seat"]["CaptainSeat"]["FacingPosition"]}), 200

@seat_bp.route('/seat/captain/backrestposition/<int:value>', methods=['POST'])
def set_captain_seat_backrest_position(value):
    if 0 <= value <= 100:
        status["Seat"]["CaptainSeat"]["BackrestPosition"] = value
        return jsonify({"status": f"Captain seat backrest position is now {value}%"}), 200
    return jsonify({"error": "Invalid backrest position value"}), 400

@seat_bp.route('/seat/captain/backrestposition', methods=['GET'])
def get_captain_seat_backrest_position():
    return jsonify({"BackrestPosition": status["Seat"]["CaptainSeat"]["BackrestPosition"]}), 200

@seat_bp.route('/seat/cocaptain/facingposition/<string:position>', methods=['POST'])
def set_co_captain_seat_facing_position(position):
    if position in ["Front", "Side", "Back", "Rotating"]:
        status["Seat"]["CoCaptainSeat"]["FacingPosition"] = position
        return jsonify({"status": f"Co-captain seat facing position is now {position}"}), 200
    return jsonify({"error": "Invalid facing position value"}), 400

@seat_bp.route('/seat/cocaptain/facingposition', methods=['GET'])
def get_co_captain_seat_facing_position():
    return jsonify({"FacingPosition": status["Seat"]["CoCaptainSeat"]["FacingPosition"]}), 200

@seat_bp.route('/seat/cocaptain/backrestposition/<int:value>', methods=['POST'])
def set_co_captain_seat_backrest_position(value):
    if 0 <= value <= 100:
        status["Seat"]["CoCaptainSeat"]["BackrestPosition"] = value
        return jsonify({"status": f"Co-captain seat backrest position is now {value}%"}), 200
    return jsonify({"error": "Invalid backrest position value"}), 400

@seat_bp.route('/seat/cocaptain/backrestposition', methods=['GET'])
def get_co_captain_seat_backrest_position():
    return jsonify({"BackrestPosition": status["Seat"]["CoCaptainSeat"]["BackrestPosition"]}), 200

# Define endpoints for retrieving the status of each seat component
@seat_bp.route('/status/seat', methods=['GET'])
def get_seat_status():
    return jsonify(status["Seat"]), 200
