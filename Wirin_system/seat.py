from flask import Flask, jsonify, request

app = Flask(__name__)

# Define the status dictionary to keep track of the states
status = {
    "Seats": [
        {
            "Name": "Captain seat (Driver Seat)",
            "Facing Position": "Front",
            "Backrest Position": 50
        },
        {
            "Name": "Co-Captain seat (Front passenger seat)",
            "Facing Position": "Front",
            "Backrest Position": 50
        }
    ]
}

# Define endpoints for setting and getting seat attributes
@app.route('/seats/<int:seat_index>/<string:attribute>/<value>', methods=['POST'])
def set_seat_attribute(seat_index: int, attribute: str, value: str):
    """Sets a specific attribute of a seat."""
    if 0 <= seat_index < len(status["Seats"]):
        if attribute == "Facing Position" and value in ["Front", "Side", "Back", "Rotating"]:
            status["Seats"][seat_index][attribute] = value
            return jsonify({"status": f"{status['Seats'][seat_index]['Name']} {attribute} is now {value}"}), 200
        elif attribute == "Backrest Position":
            try:
                value = int(value)
                if 0 <= value <= 100:
                    status["Seats"][seat_index][attribute] = value
                    return jsonify({"status": f"{status['Seats'][seat_index]['Name']} {attribute} is now {value}"}), 200
            except ValueError:
                return jsonify({"error": "Invalid value for Backrest Position"}), 400
    return jsonify({"error": "Invalid seat index or attribute"}), 400

@app.route('/seats/<int:seat_index>/<string:attribute>', methods=['GET'])
def get_seat_attribute(seat_index: int, attribute: str):
    """Gets the value of a specific attribute of a seat."""
    if 0 <= seat_index < len(status["Seats"]):
        if attribute in ["Facing Position", "Backrest Position"]:
            return jsonify({attribute: status["Seats"][seat_index][attribute]}), 200
    return jsonify({"error": "Invalid seat index or attribute"}), 400

# Define endpoint for retrieving the status of all seats
@app.route('/status/seats', methods=['GET'])
def get_seats_status():
    """Gets the status of all seats."""
    return jsonify(status["Seats"]), 200

if __name__ == '__main__':
    app.run(debug=True)