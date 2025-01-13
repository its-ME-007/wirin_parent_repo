from flask import Flask, jsonify, request, Blueprint

door_bp = Blueprint('door_bp', __name__)

door_status = "Closed"
boot_door_status = "Closed"
roof_door_status = "Closed"

@door_bp.route('/vehicledoors/door/open', methods=['POST'])
def open_door():
    global door_status
    door_status = "Open"
    return f"DoorStatus is now Open", 200

@door_bp.route('/vehicledoors/door/close', methods=['POST'])
def close_door():
    global door_status
    door_status = "Close"
    return f"DoorStatus is now Close", 200

@door_bp.route('/vehicledoors/door/opening', methods=['POST'])
def opening_door():
    global door_status
    door_status = "Opening"
    return f"DoorStatus is now Opening", 200

@door_bp.route('/vehicledoors/door/closing', methods=['POST'])
def closing_door():
    global door_status
    door_status = "Closing"
    return f"DoorStatus is now Closing", 200

@door_bp.route('/vehicledoors/door/error', methods=['POST'])
def error_door():
    global door_status
    door_status = "Error"
    return f"DoorStatus is now Error", 200

@door_bp.route('/vehicledoors/door', methods=['GET'])
def get_door_status():
    return door_status, 200

@door_bp.route('/vehicledoors/bootdoor/open', methods=['POST'])
def open_boot_door():
    global boot_door_status
    boot_door_status = "Open"
    return f"BootDoorStatus is now Open", 200

@door_bp.route('/vehicledoors/bootdoor/close', methods=['POST'])
def close_boot_door():
    global boot_door_status
    boot_door_status = "Close"
    return f"BootDoorStatus is now Close", 200

@door_bp.route('/vehicledoors/bootdoor/opening', methods=['POST'])
def opening_boot_door():
    global boot_door_status
    boot_door_status = "Opening"
    return f"BootDoorStatus is now Opening", 200

@door_bp.route('/vehicledoors/bootdoor/closing', methods=['POST'])
def closing_boot_door():
    global boot_door_status
    boot_door_status = "Closing"
    return f"BootDoorStatus is now Closing", 200

@door_bp.route('/vehicledoors/bootdoor/error', methods=['POST'])
def error_boot_door():
    global boot_door_status
    boot_door_status = "Error"
    return f"BootDoorStatus is now Error", 200

@door_bp.route('/vehicledoors/bootdoor', methods=['GET'])
def get_boot_door_status():
    return boot_door_status, 200

@door_bp.route('/vehicledoors/roofdoor/open', methods=['POST'])
def open_roof_door():
    global roof_door_status
    roof_door_status = "Open"
    return f"RoofDoorStatus is now Open", 200

@door_bp.route('/vehicledoors/roofdoor/close', methods=['POST'])
def close_roof_door():
    global roof_door_status
    roof_door_status = "Close"
    return f"RoofDoorStatus is now Close", 200

@door_bp.route('/vehicledoors/roofdoor/opening', methods=['POST'])
def opening_roof_door():
    global roof_door_status
    roof_door_status = "Opening"
    return f"RoofDoorStatus is now Opening", 200

@door_bp.route('/vehicledoors/roofdoor/closing', methods=['POST'])
def closing_roof_door():
    global roof_door_status
    roof_door_status = "Closing"
    return f"RoofDoorStatus is now Closing", 200

@door_bp.route('/vehicledoors/roofdoor/error', methods=['POST'])
def error_roof_door():
    global roof_door_status
    roof_door_status = "Error"
    return f"RoofDoorStatus is now Error", 200

@door_bp.route('/vehicledoors/roofdoor', methods=['GET'])
def get_roof_door_status():
    return roof_door_status, 200



