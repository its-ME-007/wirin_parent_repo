from flask import Flask, jsonify, request, Blueprint

bywire_bp = Blueprint('bywire_bp', __name__)

steering_status = "Open"
acc_brake_pedal_status = "Open"

@bywire_bp.route('/bywiresystem/steering/open', methods=['POST'])
def open_steering():
    global steering_status
    steering_status = "Open"
    return f"SteeringStatus is now Open", 200

@bywire_bp.route('/bywiresystem/steering/close', methods=['POST'])
def close_steering():
    global steering_status
    steering_status = "Close"
    return f"SteeringStatus is now Close", 200

@bywire_bp.route('/bywiresystem/steering/opening', methods=['POST'])
def opening_steering():
    global steering_status
    steering_status = "Opening"
    return f"SteeringStatus is now Opening", 200

@bywire_bp.route('/bywiresystem/steering/closing', methods=['POST'])
def closing_steering():
    global steering_status
    steering_status = "Closing"
    return f"SteeringStatus is now Closing", 200

@bywire_bp.route('/bywiresystem/steering/error', methods=['POST'])
def error_steering():
    global steering_status
    steering_status = "Error"
    return f"SteeringStatus is now Error", 200

@bywire_bp.route('/bywiresystem/steering', methods=['GET'])
def get_steering_status():
    return steering_status, 200

@bywire_bp.route('/bywiresystem/accbrake/open', methods=['POST'])
def open_acc_brake():
    global acc_brake_pedal_status
    acc_brake_pedal_status = "Open"
    return f"AccBrakePedalStatus is now Open", 200

@bywire_bp.route('/bywiresystem/accbrake/close', methods=['POST'])
def close_acc_brake():
    global acc_brake_pedal_status
    acc_brake_pedal_status = "Close"
    return f"AccBrakePedalStatus is now Close", 200

@bywire_bp.route('/bywiresystem/accbrake/opening', methods=['POST'])
def opening_acc_brake():
    global acc_brake_pedal_status
    acc_brake_pedal_status = "Opening"
    return f"AccBrakePedalStatus is now Opening", 200

@bywire_bp.route('/bywiresystem/accbrake/closing', methods=['POST'])
def closing_acc_brake():
    global acc_brake_pedal_status
    acc_brake_pedal_status = "Closing"
    return f"AccBrakePedalStatus is now Closing", 200

@bywire_bp.route('/bywiresystem/accbrake/error', methods=['POST'])
def error_acc_brake():
    global acc_brake_pedal_status
    acc_brake_pedal_status = "Error"
    return f"AccBrakePedalStatus is now Error", 200

@bywire_bp.route('/bywiresystem/accbrake', methods=['GET'])
def get_acc_brake_pedal_status():
    return acc_brake_pedal_status, 200



