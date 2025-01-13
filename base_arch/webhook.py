from flask import Flask, jsonify, render_template
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from maps import mapping
from song_player import song_player
from lighting_ac import lighting_ac

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 12345  # Change this to a secret key
jwt = JWTManager(app)

# Register Blueprints
app.register_blueprint(mapping)
app.register_blueprint(song_player)
app.register_blueprint(lighting_ac)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if username == 'admin' and password == 'password':  # Replace with your own auth logic
        access_token = create_access_token(identity=username)
        return jsonify({'access_token': access_token})
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    return jsonify({'message': 'Hello, authenticated user!'})

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)