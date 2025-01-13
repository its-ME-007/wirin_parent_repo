from flask import Flask, request, jsonify
import os

app = Flask(__name__)
current_vol = 0

@app.route('/volume/set', methods=['POST'])
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
    
@app.route('/volume/get', methods=['GET'])
def get_volume():
    result = f"Current volume is {current_vol}"
    return jsonify({"result": result})

@app.route('/volume/mute', methods=['POST'])
def mute():
    try:
        os.system("amixer set Master 1")
        result = "Speaker muted"
        return jsonify({"status": "success", "result": result})
    except Exception as e:
        return jsonify({"status": "error", "result": str(e)}), 500

@app.route('/volume/unmute', methods=['POST'])
def unmute():
    global current_vol
    try:
        os.system("amixer set Master 75")
        result = "Speaker unmuted"
        return jsonify({"status": "success", "result": result})
    except Exception as e:
        return jsonify({"status": "error", "result": str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True, port=5010)
