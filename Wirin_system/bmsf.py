from flask import Flask, jsonify, request, Blueprint

bms_bp = Blueprint('bms_bp', __name__)

# Define the status dictionary to keep track of the states
status = {
    "Battery": {
        "Voltage": 0,
        "Current": 0,
        "SOC": 0,
        "NumberOfCells": 0,
        "CellVoltage": 0,
        "ChargingMOSFET": "OFF",
        "DischargingMOSFET": "OFF",
        "CellMinimumVoltage": 0,
        "CellMinVoltageNumber": 0,
        "CellMaximumVoltage": 0,
        "CellMaxVoltageNumber": 0,
        "Capacity": 0,
        "ERRORStatus": 0,
        "Temperature": 0
    }
}



@bms_bp.route('/battery/<string:attribute>/<int:value>', methods=['POST'])
def set_battery_attribute(attribute, value):
    valid_ranges = {
        "voltage": (0, 100),
        "current": (-500, 500),
        "soc": (0, 100),
        "numberofcells": (0, 40),
        "cellvoltage": (0, 5),
        "cellminimumvoltage": (0, 5),
        "cellminvoltagenumber": (0, 40),
        "cellmaximumvoltage": (0, 5),
        "cellmaxvoltagenumber": (0, 40),
        "capacity": (0, 300),
        "errorstatus": (0, 255),
        "temperature": (0, 100)
    }
    
    attribute_mapping = {
        "voltage": "Voltage",
        "current": "Current",
        "soc": "SOC",
        "numberofcells": "NumberOfCells",
        "cellvoltage": "CellVoltage",
        "chargingmosfet": "ChargingMOSFET",
        "dischargingmosfet": "DischargingMOSFET",
        "cellminimumvoltage": "CellMinimumVoltage",
        "cellminvoltagenumber": "CellMinVoltageNumber",
        "cellmaximumvoltage": "CellMaximumVoltage",
        "cellmaxvoltagenumber": "CellMaxVoltageNumber",
        "capacity": "Capacity",
        "errorstatus": "ERRORStatus",
        "temperature": "Temperature"
    }
    
    if attribute not in attribute_mapping:
        return jsonify({"error": "Invalid attribute"}), 400

    if attribute in valid_ranges and not (valid_ranges[attribute][0] <= value <= valid_ranges[attribute][1]):
        return jsonify({"error": f"Invalid {attribute} value"}), 400
    
    if attribute in ["chargingmosfet", "dischargingmosfet"]:
        status["Battery"][attribute_mapping[attribute]] = "ON" if value == 1 else "OFF"
    else:
        status["Battery"][attribute_mapping[attribute]] = value
        
    return jsonify({"status": f"Battery {attribute} is now {value}"}), 200

@bms_bp.route('/battery/<string:attribute>', methods=['GET'])
def get_battery_attribute(attribute):
    attribute_mapping = {
        "voltage": "Voltage",
        "current": "Current",
        "soc": "SOC",
        "numberofcells": "NumberOfCells",
        "cellvoltage": "CellVoltage",
        "chargingmosfet": "ChargingMOSFET",
        "dischargingmosfet": "DischargingMOSFET",
        "cellminimumvoltage": "CellMinimumVoltage",
        "cellminvoltagenumber": "CellMinVoltageNumber",
        "cellmaximumvoltage": "CellMaximumVoltage",
        "cellmaxvoltagenumber": "CellMaxVoltageNumber",
        "capacity": "Capacity",
        "errorstatus": "ERRORStatus",
        "temperature": "Temperature"
    }

    if attribute not in attribute_mapping:
        return jsonify({"error": "Invalid attribute"}), 400

    return jsonify({attribute_mapping[attribute]: status["Battery"][attribute_mapping[attribute]]}), 200

# Backup Code 

'''
from flask import Flask, jsonify, Blueprint

app = Flask(__name__)

# Define the status dictionary to keep track of the states
status = {
    "Battery": {
        "Voltage": 0,
        "Current": 0,
        "SOC": 0,
        "NumberOfCells": 0,
        "CellVoltage": 0,
        "ChargingMOSFET": "OFF",
        "DischargingMOSFET": "OFF",
        "CellMinimumVoltage": 0,
        "CellMinVoltageNumber": 0,
        "CellMaximumVoltage": 0,
        "CellMaxVoltageNumber": 0,
        "Capacity": 0,
        "ERRORStatus": 0,
        "Temperature": 0
    }
}

bms_bp = Blueprint('bms_bp', __name__)

@bms_bp.route('/battery/voltage/<int:value>', methods=['POST'])
def set_battery_voltage(value):
    if 0 <= value <= 100:
        status["Battery"]["Voltage"] = value
        return jsonify({"status": f"Battery voltage is now {value}V"}), 200
    return jsonify({"error": "Invalid voltage value"}), 400

@bms_bp.route('/battery/voltage', methods=['GET'])
def get_battery_voltage():
    return jsonify({"Voltage": status["Battery"]["Voltage"]}), 200

@bms_bp.route('/battery/current/<int:value>', methods=['POST'])
def set_battery_current(value):
    if -500 <= value <= 500:
        status["Battery"]["Current"] = value
        return jsonify({"status": f"Battery current is now {value}A"}), 200
    return jsonify({"error": "Invalid current value"}), 400

@bms_bp.route('/battery/current', methods=['GET'])
def get_battery_current():
    return jsonify({"Current": status["Battery"]["Current"]}), 200

@bms_bp.route('/battery/soc/<int:value>', methods=['POST'])
def set_battery_soc(value):
    if 0 <= value <= 100:
        status["Battery"]["SOC"] = value
        return jsonify({"status": f"Battery SOC is now {value}%"}), 200
    return jsonify({"error": "Invalid SOC value"}), 400

@bms_bp.route('/battery/soc', methods=['GET'])
def get_battery_soc():
    return jsonify({"SOC": status["Battery"]["SOC"]}), 200

@bms_bp.route('/battery/numberofcells/<int:value>', methods=['POST'])
def set_battery_number_of_cells(value):
    if 0 <= value <= 40:
        status["Battery"]["NumberOfCells"] = value
        return jsonify({"status": f"Number of battery cells is now {value}"}), 200
    return jsonify({"error": "Invalid number of cells value"}), 400

@bms_bp.route('/battery/numberofcells', methods=['GET'])
def get_battery_number_of_cells():
    return jsonify({"NumberOfCells": status["Battery"]["NumberOfCells"]}), 200

@bms_bp.route('/battery/cellvoltage/<int:value>', methods=['POST'])
def set_battery_cell_voltage(value):
    if 0 <= value <= 5:
        status["Battery"]["CellVoltage"] = value
        return jsonify({"status": f"Battery cell voltage is now {value}V"}), 200
    return jsonify({"error": "Invalid cell voltage value"}), 400

@bms_bp.route('/battery/cellvoltage', methods=['GET'])
def get_battery_cell_voltage():
    return jsonify({"CellVoltage": status["Battery"]["CellVoltage"]}), 200

@bms_bp.route('/battery/chargingmosfet/<int:state>', methods=['POST'])
def set_battery_charging_mosfet(state):
    if state in [0, 1]:
        status["Battery"]["ChargingMOSFET"] = "ON" if state == 1 else "OFF"
        return jsonify({"status": f"Battery charging MOSFET is now {'ON' if state == 1 else 'OFF'}"}), 200
    return jsonify({"error": "Invalid MOSFET state"}), 400

@bms_bp.route('/battery/chargingmosfet', methods=['GET'])
def get_battery_charging_mosfet():
    return jsonify({"ChargingMOSFET": status["Battery"]["ChargingMOSFET"]}), 200

@bms_bp.route('/battery/dischargingmosfet/<int:state>', methods=['POST'])
def set_battery_discharging_mosfet(state):
    if state in [0, 1]:
        status["Battery"]["DischargingMOSFET"] = "ON" if state == 1 else "OFF"
        return jsonify({"status": f"Battery discharging MOSFET is now {'ON' if state == 1 else 'OFF'}"}), 200
    return jsonify({"error": "Invalid MOSFET state"}), 400

@bms_bp.route('/battery/dischargingmosfet', methods=['GET'])
def get_battery_discharging_mosfet():
    return jsonify({"DischargingMOSFET": status["Battery"]["DischargingMOSFET"]}), 200

@bms_bp.route('/battery/cellminimumvoltage/<int:value>', methods=['POST'])
def set_battery_cell_minimum_voltage(value):
    if 0 <= value <= 5:
        status["Battery"]["CellMinimumVoltage"] = value
        return jsonify({"status": f"Battery cell minimum voltage is now {value}V"}), 200
    return jsonify({"error": "Invalid minimum voltage value"}), 400

@bms_bp.route('/battery/cellminimumvoltage', methods=['GET'])
def get_battery_cell_minimum_voltage():
    return jsonify({"CellMinimumVoltage": status["Battery"]["CellMinimumVoltage"]}), 200

@bms_bp.route('/battery/cellminvoltagenumber/<int:value>', methods=['POST'])
def set_battery_cell_min_voltage_number(value):
    if 0 <= value <= 40:
        status["Battery"]["CellMinVoltageNumber"] = value
        return jsonify({"status": f"Battery cell minimum voltage number is now {value}"}), 200
    return jsonify({"error": "Invalid minimum voltage number value"}), 400

@bms_bp.route('/battery/cellminvoltagenumber', methods=['GET'])
def get_battery_cell_min_voltage_number():
    return jsonify({"CellMinVoltageNumber": status["Battery"]["CellMinVoltageNumber"]}), 200

@bms_bp.route('/battery/cellmaximumvoltage/<int:value>', methods=['POST'])
def set_battery_cell_maximum_voltage(value):
    if 0 <= value <= 5:
        status["Battery"]["CellMaximumVoltage"] = value
        return jsonify({"status": f"Battery cell maximum voltage is now {value}V"}), 200
    return jsonify({"error": "Invalid maximum voltage value"}), 400

@bms_bp.route('/battery/cellmaximumvoltage', methods=['GET'])
def get_battery_cell_maximum_voltage():
    return jsonify({"CellMaximumVoltage": status["Battery"]["CellMaximumVoltage"]}), 200

@bms_bp.route('/battery/cellmaxvoltagenumber/<int:value>', methods=['POST'])
def set_battery_cell_max_voltage_number(value):
    if 0 <= value <= 40:
        status["Battery"]["CellMaxVoltageNumber"] = value
        return jsonify({"status": f"Battery cell maximum voltage number is now {value}"}), 200
    return jsonify({"error": "Invalid maximum voltage number value"}), 400

@bms_bp.route('/battery/cellmaxvoltagenumber', methods=['GET'])
def get_battery_cell_max_voltage_number():
    return jsonify({"CellMaxVoltageNumber": status["Battery"]["CellMaxVoltageNumber"]}), 200

@bms_bp.route('/battery/capacity/<int:value>', methods=['POST'])
def set_battery_capacity(value):
    if 0 <= value <= 300:
        status["Battery"]["Capacity"] = value
        return jsonify({"status": f"Battery capacity is now {value}Ah"}), 200
    return jsonify({"error": "Invalid capacity value"}), 400

@bms_bp.route('/battery/capacity', methods=['GET'])
def get_battery_capacity():
    return jsonify({"Capacity": status["Battery"]["Capacity"]}), 200

@bms_bp.route('/battery/errorstatus/<int:value>', methods=['POST'])
def set_battery_error_status(value):
    if 0 <= value <= 255:
        status["Battery"]["ERRORStatus"] = value
        return jsonify({"status": f"Battery error status is now {value}"}), 200
    return jsonify({"error": "Invalid error status value"}), 400

@bms_bp.route('/battery/errorstatus', methods=['GET'])
def get_battery_error_status():
    return jsonify({"ERRORStatus": status["Battery"]["ERRORStatus"]}), 200

@bms_bp.route('/battery/temperature/<int:value>', methods=['POST'])
def set_battery_temperature(value):
    if 0 <= value <= 100:
        status["Battery"]["Temperature"] = value
        return jsonify({"status": f"Battery temperature is now {value}°C"}), 200
    return jsonify({"error": "Invalid temperature value"}), 400

@bms_bp.route('/battery/temperature', methods=['GET'])
def get_battery_temperature():
    return jsonify({"Temperature": status["Battery"]["Temperature"]}), 200





'''