from flask import Blueprint, jsonify, request

lvl1_cu_bp = Blueprint('lvl1_cu', __name__)

# Define the status dictionary to keep track of the states
lvl1_status = {
    "LEVEL1_CU": {
        "ECU2-ICU": {"Heartbeat": 0, "Status": "N/A"},
        "ECU6-VHMS": {"Heartbeat": 0, "Status": "N/A"},
        "17- Monitor and Processor": {"Heartbeat": "N/A", "Status": "ACTIVE/PROCESSING/BUSY"},
        "MPU - Motion Planner": {"Heartbeat": "N/A", "Status": "PROCESSING/ACTIVE/BUSY/OVERLOAD"}
    }
}

# Define endpoints for setting and getting ECU status
@lvl1_cu_bp.route('/controlunitstatus/<ecu>/<attribute>/<value>', methods=['POST'])
def set_ecu_status(ecu, attribute, value):
    if ecu in lvl1_status["LEVEL1_CU"]:
        if attribute in lvl1_status["LEVEL1_CU"][ecu]:
            if attribute == "Heartbeat":
                if value == "1":
                    lvl1_status["LEVEL1_CU"][ecu][attribute] = 1
                elif value == "0":
                    lvl1_status["LEVEL1_CU"][ecu][attribute] = 0
                else:
                    return jsonify({"error": "Invalid heartbeat value"}), 400
            else:
                lvl1_status["LEVEL1_CU"][ecu][attribute] = value
            return jsonify({"status": f"{ecu} {attribute} is now {value}"}), 200
    return jsonify({"error": "Invalid ECU or attribute"}), 400

@lvl1_cu_bp.route('/controlunitstatus/<ecu>/<attribute>', methods=['GET'])
def get_ecu_status(ecu, attribute):
    if ecu in lvl1_status["LEVEL1_CU"]:
        if attribute in lvl1_status["LEVEL1_CU"][ecu]:
            if attribute == "Heartbeat":
                if lvl1_status["LEVEL1_CU"][ecu][attribute] == 1:
                    return jsonify({attribute: "1"}), 200
                elif lvl1_status["LEVEL1_CU"][ecu][attribute] == 0:
                    return jsonify({attribute: "0"}), 200
            else:
                return jsonify({attribute: lvl1_status["LEVEL1_CU"][ecu][attribute]}), 200
    return jsonify({"error": "Invalid ECU or attribute"}), 400

# Define endpoint for retrieving the overall control unit status
@lvl1_cu_bp.route('/status/lvl1controlunitstatus', methods=['GET'])
def get_lvl1_control_unit_status():
    return jsonify({"LEVEL1_CU": lvl1_status["LEVEL1_CU"]}), 200