from flask import Flask, jsonify, request

app = Flask(__name__)
speed = {"c_speed" : 0}

@app.route('/post/<speed>', methods=["POST"])
def speed_post(speed):
    try:
        speed["c_speed"] = int(speed)
    except ValueError:
        return jsonify({"error": "Invalid speed value"}), 400
    return speed

@app.route('/get', methods=["GET"])
def speed_get():
    return str(speed["c_speed"])

if __name__ == "__main__":
    app.run(debug=True, port=5007)


