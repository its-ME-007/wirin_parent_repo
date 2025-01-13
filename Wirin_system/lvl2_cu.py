from flask import Blueprint, jsonify, request

lvl2_cu_bp = Blueprint('lvl2_cu', __name__)

# Define the status dictionary to keep track of the states
lvl2_status = {
    "LEVEL2_CU": {
        "ECU1-VCU": {"Heartbeat": 0, "ActiveSoul": "MAIN/SHADOW"},
        "ECUX-FCU": {"Heartbeat": 0, "Status": "N/A"},
        "ECU3-DoorECU": {"Heartbeat": 0, "ActiveSoul": "MAIN/SHADOW"},
        "ECU4-RPi-OUT": {"Heartbeat": 0, "Status": "N/A"},
        "ECU5-RPi-IN": {"Heartbeat": 0, "Status": "N/A"},
        "ECU7-HVAC": {"Heartbeat": 0, "Status": "N/A"},
        "ECU8-USU": {"Heartbeat": 0, "Status": "N/A"},
        "ECU9-LCU": {"Heartbeat": 0, "Status": "N/A"},
        "ECU10-DashboardECU": {"Heartbeat": 0, "Status": "N/A"},
        "ECU11-TableECU": {"Heartbeat": 0, "Status": "N/A"}
    }
}

# Define endpoints for setting and getting ECU status
@lvl2_cu_bp.route('/controlunitstatus/<ecu>/<attribute>/<value>', methods=['POST'])
def set_ecu_status(ecu, attribute, value):
    if ecu in lvl2_status["LEVEL2_CU"]:
        if attribute in lvl2_status["LEVEL2_CU"][ecu]:
            if attribute == "Heartbeat":
                if value == "1":
                    lvl2_status["LEVEL2_CU"][ecu][attribute] = 1
                elif value == "0":
                    lvl2_status["LEVEL2_CU"][ecu][attribute] = 0
                else:
                    return jsonify({"error": "Invalid heartbeat value"}), 400
            else:
                lvl2_status["LEVEL2_CU"][ecu][attribute] = value
            return jsonify({"status": f"{ecu} {attribute} is now {value}"}), 200
    return jsonify({"error": "Invalid ECU or attribute"}), 400

@lvl2_cu_bp.route('/controlunitstatus/<ecu>/<attribute>', methods=['GET'])
def get_ecu_status(ecu, attribute):
    if ecu in lvl2_status["LEVEL2_CU"]:
        if attribute in lvl2_status["LEVEL2_CU"][ecu]:
            if attribute == "Heartbeat":
                if lvl2_status["LEVEL2_CU"][ecu][attribute] == 1:
                    return jsonify({attribute: "1"}), 200
                elif lvl2_status["LEVEL2_CU"][ecu][attribute] == 0:
                    return jsonify({attribute: "0"}), 200
            else:
                return jsonify({attribute: lvl2_status["LEVEL2_CU"][ecu][attribute]}), 200
    return jsonify({"error": "Invalid ECU or attribute"}), 400

# Define endpoint for retrieving the overall control unit status
@lvl2_cu_bp.route('/status/lvl2controlunitstatus', methods=['GET'])
def get_lvl2_control_unit_status():
    return jsonify({"LEVEL2_CU": lvl2_status["LEVEL2_CU"]}), 200