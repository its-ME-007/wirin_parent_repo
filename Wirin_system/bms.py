from flask import Flask, jsonify, request
import threading

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

# Define threading functions for each component
def battery_voltage_thread():
    @app.route('/battery/voltage/<int:value>', methods=['POST'])
    def set_battery_voltage(value):
        if 0 <= value <= 100:
            status["Battery"]["Voltage"] = value
            return jsonify({"status": f"Battery voltage is now {value}V"}), 200
        return jsonify({"error": "Invalid voltage value"}), 400

    @app.route('/battery/voltage', methods=['GET'])
    def get_battery_voltage():
        return jsonify({"Voltage": status["Battery"]["Voltage"]}), 200

def battery_current_thread():
    @app.route('/battery/current/<int:value>', methods=['POST'])
    def set_battery_current(value):
        if -500 <= value <= 500:
            status["Battery"]["Current"] = value
            return jsonify({"status": f"Battery current is now {value}A"}), 200
        return jsonify({"error": "Invalid current value"}), 400

    @app.route('/battery/current', methods=['GET'])
    def get_battery_current():
        return jsonify({"Current": status["Battery"]["Current"]}), 200

def battery_soc_thread():
    @app.route('/battery/soc/<int:value>', methods=['POST'])
    def set_battery_soc(value):
        if 0 <= value <= 100:
            status["Battery"]["SOC"] = value
            return jsonify({"status": f"Battery SOC is now {value}%"}), 200
        return jsonify({"error": "Invalid SOC value"}), 400

    @app.route('/battery/soc', methods=['GET'])
    def get_battery_soc():
        return jsonify({"SOC": status["Battery"]["SOC"]}), 200

def battery_number_of_cells_thread():
    @app.route('/battery/numberofcells/<int:value>', methods=['POST'])
    def set_battery_number_of_cells(value):
        if 0 <= value <= 40:
            status["Battery"]["NumberOfCells"] = value
            return jsonify({"status": f"Number of battery cells is now {value}"}), 200
        return jsonify({"error": "Invalid number of cells value"}), 400

    @app.route('/battery/numberofcells', methods=['GET'])
    def get_battery_number_of_cells():
        return jsonify({"NumberOfCells": status["Battery"]["NumberOfCells"]}), 200

def battery_cell_voltage_thread():
    @app.route('/battery/cellvoltage/<int:value>', methods=['POST'])
    def set_battery_cell_voltage(value):
        if 0 <= value <= 5:
            status["Battery"]["CellVoltage"] = value
            return jsonify({"status": f"Battery cell voltage is now {value}V"}), 200
        return jsonify({"error": "Invalid cell voltage value"}), 400

    @app.route('/battery/cellvoltage', methods=['GET'])
    def get_battery_cell_voltage():
        return jsonify({"CellVoltage": status["Battery"]["CellVoltage"]}), 200

def battery_charging_mosfet_thread():
    @app.route('/battery/chargingmosfet/<int:state>', methods=['POST'])
    def set_battery_charging_mosfet(state):
        if state in [0, 1]:
            status["Battery"]["ChargingMOSFET"] = state
            return jsonify({"status": f"Battery charging MOSFET is now {'ON' if state == 1 else 'OFF'}"}), 200
        return jsonify({"error": "Invalid MOSFET state"}), 400

    @app.route('/battery/chargingmosfet', methods=['GET'])
    def get_battery_charging_mosfet():
        return jsonify({"ChargingMOSFET": status["Battery"]["ChargingMOSFET"]}), 200

def battery_discharging_mosfet_thread():
    @app.route('/battery/dischargingmosfet/<int:state>', methods=['POST'])
    def set_battery_discharging_mosfet(state):
        if state in [0, 1]:
            status["Battery"]["DischargingMOSFET"] = state
            return jsonify({"status": f"Battery discharging MOSFET is now {'ON' if state == 1 else 'OFF'}"}), 200
        return jsonify({"error": "Invalid MOSFET state"}), 400

    @app.route('/battery/dischargingmosfet', methods=['GET'])
    def get_battery_discharging_mosfet():
        return jsonify({"DischargingMOSFET": status["Battery"]["DischargingMOSFET"]}), 200

def battery_cell_minimum_voltage_thread():
    @app.route('/battery/cellminimumvoltage/<int:value>', methods=['POST'])
    def set_battery_cell_minimum_voltage(value):
        if 0 <= value <= 5:
            status["Battery"]["CellMinimumVoltage"] = value
            return jsonify({"status": f"Battery cell minimum voltage is now {value}V"}), 200
        return jsonify({"error": "Invalid minimum voltage value"}), 400

    @app.route('/battery/cellminimumvoltage', methods=['GET'])
    def get_battery_cell_minimum_voltage():
        return jsonify({"CellMinimumVoltage": status["Battery"]["CellMinimumVoltage"]}), 200

def battery_cell_min_voltage_number_thread():
    @app.route('/battery/cellminvoltagenumber/<int:value>', methods=['POST'])
    def set_battery_cell_min_voltage_number(value):
        if 0 <= value <= 40:
            status["Battery"]["CellMinVoltageNumber"] = value
            return jsonify({"status": f"Battery cell minimum voltage number is now {value}"}), 200
        return jsonify({"error": "Invalid minimum voltage number value"}), 400

    @app.route('/battery/cellminvoltagenumber', methods=['GET'])
    def get_battery_cell_min_voltage_number():
        return jsonify({"CellMinVoltageNumber": status["Battery"]["CellMinVoltageNumber"]}), 200

def battery_cell_maximum_voltage_thread():
    @app.route('/battery/cellmaximumvoltage/<int:value>', methods=['POST'])
    def set_battery_cell_maximum_voltage(value):
        if 0 <= value <= 5:
            status["Battery"]["CellMaximumVoltage"] = value
            return jsonify({"status": f"Battery cell maximum voltage is now {value}V"}), 200
        return jsonify({"error": "Invalid maximum voltage value"}), 400

    @app.route('/battery/cellmaximumvoltage', methods=['GET'])
    def get_battery_cell_maximum_voltage():
        return jsonify({"CellMaximumVoltage": status["Battery"]["CellMaximumVoltage"]}), 200

def battery_cell_max_voltage_number_thread():
    @app.route('/battery/cellmaxvoltagenumber/<int:value>', methods=['POST'])
    def set_battery_cell_max_voltage_number(value):
        if 0 <= value <= 40:
            status["Battery"]["CellMaxVoltageNumber"] = value
            return jsonify({"status": f"Battery cell maximum voltage number is now {value}"}), 200
        return jsonify({"error": "Invalid maximum voltage number value"}), 400

    @app.route('/battery/cellmaxvoltagenumber', methods=['GET'])
    def get_battery_cell_max_voltage_number():
        return jsonify({"CellMaxVoltageNumber": status["Battery"]["CellMaxVoltageNumber"]}), 200

def battery_capacity_thread():
    @app.route('/battery/capacity/<int:value>', methods=['POST'])
    def set_battery_capacity(value):
        if 0 <= value <= 300:
            status["Battery"]["Capacity"] = value
            return jsonify({"status": f"Battery capacity is now {value}Ah"}), 200
        return jsonify({"error": "Invalid capacity value"}), 400

    @app.route('/battery/capacity', methods=['GET'])
    def get_battery_capacity():
        return jsonify({"Capacity": status["Battery"]["Capacity"]}), 200

def battery_error_status_thread():
    @app.route('/battery/errorstatus/<int:value>', methods=['POST'])
    def set_battery_error_status(value):
        if 0 <= value <= 255:
            status["Battery"]["ERRORStatus"] = value
            return jsonify({"status": f"Battery error status is now {value}"}), 200
        return jsonify({"error": "Invalid error status value"}), 400

    @app.route('/battery/errorstatus', methods=['GET'])
    def get_battery_error_status():
        return jsonify({"ERRORStatus": status["Battery"]["ERRORStatus"]}), 200

def battery_temperature_thread():
    @app.route('/battery/temperature/<int:value>', methods=['POST'])
    def set_battery_temperature(value):
        if 0 <= value <= 100:
            status["Battery"]["Temperature"] = value
            return jsonify({"status": f"Battery temperature is now {value}°C"}), 200
        return jsonify({"error": "Invalid temperature value"}), 400

    @app.route('/battery/temperature', methods=['GET'])
    def get_battery_temperature():
        return jsonify({"Temperature": status["Battery"]["Temperature"]}), 200

# Define endpoints for retrieving the status of each component
@app.route('/status/battery', methods=['GET'])
def get_battery_status():
    return jsonify(status["Battery"]), 200

# Start the threads
threads = []
threads.append(threading.Thread(target=battery_voltage_thread))
threads.append(threading.Thread(target=battery_current_thread))
threads.append(threading.Thread(target=battery_soc_thread))
threads.append(threading.Thread(target=battery_number_of_cells_thread))
threads.append(threading.Thread(target=battery_cell_voltage_thread))
threads.append(threading.Thread(target=battery_charging_mosfet_thread))
threads.append(threading.Thread(target=battery_discharging_mosfet_thread))
threads.append(threading.Thread(target=battery_cell_minimum_voltage_thread))
threads.append(threading.Thread(target=battery_cell_min_voltage_number_thread))
threads.append(threading.Thread(target=battery_cell_maximum_voltage_thread))
threads.append(threading.Thread(target=battery_cell_max_voltage_number_thread))
threads.append(threading.Thread(target=battery_capacity_thread))
threads.append(threading.Thread(target=battery_error_status_thread))
threads.append(threading.Thread(target=battery_temperature_thread))

for thread in threads:
    thread.start()

if __name__ == '__main__':
    app.run(debug=True)