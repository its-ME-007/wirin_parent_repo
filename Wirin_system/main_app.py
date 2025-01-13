from threading import Thread
from flask import Flask, jsonify
from intlight import int_lighting_bp
from obc import obc_bp
from extlight import ext_lighting_bp
from cardata1 import cardata1_bp
from cardata2 import cardata2_bp
from cardata3 import cardata3_bp
from cardata4 import cardata4_bp, update_globalclock
from tablestat import table_bp
from llc import control_settings_bp
from pidstatus import pid_status_bp
from masterpid import master_pid_values_bp
from vehicledoors import door_bp
from bywiresystem import bywire_bp
from Tv import tv_bp
from hvac import hvac_bp
from lvl1_cu import lvl1_cu_bp
from lvl2_cu import lvl2_cu_bp
from carmode import carmode_bp
from tyre import tyre_bp
from seatf import seat_bp
from bmsf import bms_bp

def create_main_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
         return jsonify({
            "message": "Welcome to the Modular Request Resolver API",
            "port directory": [
                "5000: Main Application: The main Flask app providing a welcome message and listing the available endpoints.",
                "5001: Combined Lighting Application: This app handles internal and external lighting functionalities by registering int_lighting_bp and ext_lighting_bp blueprints.",
                "5002: On-Board Computer (OBC) Application: This app handles functionalities related to the vehicle's on-board computer using the obc_bp blueprint.",
                "5003: Car Data Application: This app handles car data functionalities by registering blueprints cardata1_bp, cardata2_bp, cardata3_bp, and cardata4_bp.",
                "5004: Table Statistics Application: This app handles functionalities related to table statistics using the table_bp blueprint.",
                "5005: Control Settings Application: This app handles control settings and PID statuses by registering blueprints control_settings_bp, master_pid_values_bp, and pid_status_bp.",
                "5006: Vehicle Status Application: This app handles various vehicle status functionalities by registering blueprints door_bp, bywire_bp, carmode_bp, and tyre_bp.",
                "5007: Tyre Status Application: This app specifically handles functionalities related to tyre status using the tyre_bp blueprint.",
                "5008: Control Unit Status Application: This app handles the status of various control units by registering blueprints lvl1_cu_bp and lvl2_cu_bp.",
                "5009: HVAC Application: This app handles functionalities related to the HVAC system using the hvac_bp blueprint.",
                "5010: Seat Status Application: This app handles functionalities related to seat status using the seat_bp blueprint.",
                "5011: Battery Management System (BMS) Application: This app handles functionalities related to the battery management system using the bms_bp blueprint."
            ]
        })

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({"error": "Page not found"}), 404

    return app

def create_lighting_app():
    app = Flask(__name__)
    app.register_blueprint(int_lighting_bp)
    app.register_blueprint(ext_lighting_bp)
    return app

def create_obc_app():
    app = Flask(__name__)
    app.register_blueprint(obc_bp)
    return app

def create_cardata_app():
    app = Flask(__name__)
    app.register_blueprint(cardata1_bp)
    app.register_blueprint(cardata2_bp)
    app.register_blueprint(cardata3_bp)
    app.register_blueprint(cardata4_bp)
    return app

def create_controlsettings_app():
    app = Flask(__name__)
    app.register_blueprint(control_settings_bp)
    app.register_blueprint(master_pid_values_bp)
    app.register_blueprint(pid_status_bp)
    return app

def create_table_app():
    app = Flask(__name__)
    app.register_blueprint(table_bp)
    return app

def create_vehiclestatus_app():
    app = Flask(__name__)
    app.register_blueprint(door_bp)
    app.register_blueprint(tv_bp)
    app.register_blueprint(bywire_bp)
    app.register_blueprint(carmode_bp)
    return app

def create_tyre_app():
    app = Flask(__name__)
    app.register_blueprint(tyre_bp)
    return app

def create_controlunitstatus_app():
    app = Flask(__name__)
    app.register_blueprint(lvl1_cu_bp)
    app.register_blueprint(lvl2_cu_bp)
    return app

def create_hvac_app():
    app = Flask(__name__)
    app.register_blueprint(hvac_bp)
    return app


def create_seat_app():
    app = Flask(__name__)
    app.register_blueprint(seat_bp)
    return app

def create_bms_app():
    app = Flask(__name__)
    app.register_blueprint(bms_bp)
    return app

def run_service(app, port):
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    # Create all the Flask applications
    main_app = create_main_app()
    lighting_app = create_lighting_app()  # Combined lighting application
    obc_app = create_obc_app()
    cardata_app = create_cardata_app()
    table_app = create_table_app()
    control_setting_app = create_controlsettings_app()
    vehiclestatus_app = create_vehiclestatus_app()
    tyre_app = create_tyre_app()
    controlunitstatus_app = create_controlunitstatus_app()
    hvac_app = create_hvac_app()
    seat_app = create_seat_app()
    bms_app = create_bms_app()

    # Start services on specific ports
    main_thread = Thread(target=run_service, args=(main_app, 5000))        # Main app on port 5000
    lighting_thread = Thread(target=run_service, args=(lighting_app, 5001))  # Combined lighting on port 5001
    obc_thread = Thread(target=run_service, args=(obc_app, 5002))          # OBC on port 5002
    cardata_thread = Thread(target=run_service, args=(cardata_app, 5003))  # Cardata1 on port 5003
    table_thread = Thread(target=run_service, args=(table_app, 5004))      # Table statistics on port 5004
    control_thread = Thread(target=run_service, args=(control_setting_app, 5005))  # Control settings on port 5005
    vehiclestatus_thread = Thread(target=run_service, args=(vehiclestatus_app, 5006))  # Vehicle status on port 5006
    tyre_thread = Thread(target=run_service, args=(tyre_app, 5007))        # Tyre status on port 5007
    controlunitstatus_thread = Thread(target=run_service, args=(controlunitstatus_app, 5008))  # Control unit status on port 5008
    hvac_thread = Thread(target=run_service, args=(hvac_app, 5009))        # HVAC on port 5009
    seat_thread = Thread(target=run_service, args=(seat_app, 5010))        # Seat status on port 5010
    bms_thread = Thread(target=run_service, args=(bms_app, 5011))         # Battery Management System on port 5011
    globalclock_thread = Thread(target=update_globalclock)                # Global clock (no port)

    # Start all threads
    main_thread.start()
    lighting_thread.start()
    obc_thread.start()
    cardata_thread.start()
    table_thread.start()
    control_thread.start()
    vehiclestatus_thread.start()
    tyre_thread.start()
    controlunitstatus_thread.start()
    hvac_thread.start()
    seat_thread.start()
    bms_thread.start()
    globalclock_thread.start()

    # Ensure all threads finish
    main_thread.join()
    lighting_thread.join()
    obc_thread.join()
    cardata_thread.join()
    table_thread.join()
    control_thread.join()
    vehiclestatus_thread.join()
    tyre_thread.join()
    controlunitstatus_thread.join()
    hvac_thread.join()
    seat_thread.join()
    bms_thread.join()
    globalclock_thread.join()
