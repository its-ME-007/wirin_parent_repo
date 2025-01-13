from flask import Blueprint, jsonify, request

song_player = Blueprint('song_player', __name__)

@song_player.route('/song/play', methods=['POST'])
def play_song():
    data = request.json
    song_id = data.get('song_id')
    if not song_id:
        return jsonify({"error": "Song ID is required"}), 400
    result = f"Playing song with ID {song_id}"
    return jsonify({"result": result})

@song_player.route('/song/stop', methods=['POST'])
def stop_song():
    result = "Stopping song"
    return jsonify({"result": result})
