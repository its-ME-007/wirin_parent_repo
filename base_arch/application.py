from flask import Flask, jsonify
from lighting_ac import lighting_bp
from maps import mapping_bp
from ac import ac_bp
from door import door_bp
from speak1 import vol_bp

def create_main_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return jsonify({
            "message": "Welcome to the Modular Request Resolver API",
            "endpoints": [
                "5001/lighting/set",
                "5001/lighting/get",
                "5002/mapping/directions?origin=<origin>&destination=<destination>",
                "5003/ac/set",
                "5003/ac/get",
                "5004/sound/set",
                "5004/sound/get"
            ]
        })

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({"error": "Page not found"}), 404

    return app

def create_lighting_app():
    app = Flask(__name__)
    app.register_blueprint(lighting_bp, url_prefix='/api')
    return app

def create_mapping_app():
    app = Flask(__name__)
    app.register_blueprint(mapping_bp, url_prefix='/api')
    return app

def create_ac_app():
    app = Flask(__name__)
    app.register_blueprint(ac_bp, url_prefix='/api')
    return app

def create_sound_app():
    app = Flask(__name__)
    app.register_blueprint(vol_bp, url_prefix='/api')
    return app

if __name__ == '__main__':
    main_app = create_main_app()
    lighting_app = create_lighting_app()
    mapping_app = create_mapping_app()
    ac_app = create_ac_app()
    vol_app = create_sound_app()

    # You could run each app in separate Gunicorn commands instead of threads
