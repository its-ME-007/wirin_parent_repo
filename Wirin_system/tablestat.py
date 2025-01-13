
from flask import Flask, jsonify, request, Blueprint

table_bp = Blueprint('table_status', __name__)

status = {
    "TableStat": {
        "tableheight": 0,
        "tablestatus": "Closed",
        "tablelamp": 0,
        "tablelampbrightness": 0
    }
}

def check_limits(value, min_val, max_val, name):
    if value < min_val or value > max_val:
        return jsonify({"Error": f"{name} value {value} is out of range ({min_val} to {max_val})"}), 400
    return None


@table_bp.route('/Tablestatus/tableheight/post', methods=['POST'])

def table_height_post():
    data = request.json
    height = data.get("tableheight")
    if height is None:
        return jsonify({"Error": "tableheight not provided"}), 400
    error = check_limits(height, 0, 100, "tableheight")
    if error:
        return error
    status["TableStat"]["tableheight"] = height
    return jsonify({"tableheight": height}), 200


@table_bp.route('/Tablestatus/tableheight/get', methods=['GET'])
def table_height_get():
    return jsonify({"tableheight": status["TableStat"]["tableheight"]}), 200

@table_bp.route('/Tablestatus/table/post', methods=['POST'])

def table_post():
    data = request.json
    tablestatus = data.get("tablestatus")
    if tablestatus is None:
        return jsonify({"Error": "tablestatus not provided"}), 400
    if tablestatus not in ["Open", "Closed", "Opening", "Closing", "Error"]:
        return jsonify({"Error": "Invalid tablestatus value"}), 400
    status["TableStat"]["tablestatus"] = tablestatus
    return jsonify({"tablestatus": tablestatus}), 200


@table_bp.route('/Tablestatus/table/get', methods=['GET'])
def table_get():
    return jsonify({"tablestatus": status["TableStat"]["tablestatus"]}), 200

@table_bp.route('/Tablestatus/tablelamp/post', methods=['POST'])

def table_lamp_post():
    data = request.json
    tablelamp = data.get("tablelamp")
    if tablelamp is None:
        return jsonify({"Error": "tablelamp not provided"}), 400
    if tablelamp not in [0, 1]:
        return jsonify({"Error": "Invalid tablelamp value, must be 0 (off) or 1 (on)"}), 400
    status["TableStat"]["tablelamp"] = tablelamp
    tablelamp_status = "on" if tablelamp == 1 else "off"
    return jsonify({"tablelamp": tablelamp, "tablelamp_status": tablelamp_status}), 200


@table_bp.route('/Tablestatus/tablelamp/get', methods=['GET'])
def table_lamp_get():
    tablelamp_status = "on" if status["TableStat"]["tablelamp"] == 1 else "off"
    return jsonify({"tablelamp_status": tablelamp_status}), 200

@table_bp.route('/Tablestatus/tablelampbrightness/post', methods=['POST'])

def table_lamp_brightness_post():
    data = request.json
    brightness = data.get("tablelampbrightness")
    if brightness is None:
        return jsonify({"Error": "tablelampbrightness not provided"}), 400
    error = check_limits(brightness, 0, 100, "tablelampbrightness")
    if error:
        return error
    status["TableStat"]["tablelampbrightness"] = brightness
    return jsonify({"tablelampbrightness": brightness}), 200


@table_bp.route('/Tablestatus/tablelampbrightness/get', methods=['GET'])
def table_lamp_brightness_get():
    return jsonify({"tablelampbrightness": status["TableStat"]["tablelampbrightness"]}), 200
'''
if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(table_bp)
    app.run(debug=True)'''

