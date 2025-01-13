from flask import Flask, jsonify
from maps import mapping
from song_player import song_player
from lighting_ac import lighting_ac

# Create separate Flask applications for each blueprint
app_mapping = Flask('mapping')
app_song_player = Flask('song_player')
app_lighting_ac = Flask('lighting_ac')

# Register Blueprints
app_mapping.register_blueprint(mapping)
app_song_player.register_blueprint(song_player)
app_lighting_ac.register_blueprint(lighting_ac)

@app_mapping.route('/')
def index_mapping():
    return jsonify({
        "message": "Welcome to the Mapping API",
        "endpoints": [
            "/mapping/directions?origin=<origin>&destination=<destination>"
        ]
    })

@app_song_player.route('/')
def index_song_player():
    return jsonify({
        "message": "Welcome to the Song Player API",
        "endpoints": [
            "/song/play",
            "/song/stop"
        ]
    })

@app_lighting_ac.route('/')
def index_lighting_ac():
    return jsonify({
        "message": "Welcome to the Lighting AC API",
        "endpoints": [
            "/lighting/set",
            "/ac/set",
            "/lighting/get",
            "/ac/get"
        ]
    })

@app_mapping.errorhandler(404)
@app_song_player.errorhandler(404)
@app_lighting_ac.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found"}), 404

if __name__ == '__main__':
    app_mapping.run(debug=True, port=5001)
    app_song_player.run(debug=True, port=5002)
    app_lighting_ac.run(debug=True, port=5003)