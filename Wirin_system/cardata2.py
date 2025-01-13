from flask import Blueprint, jsonify, request

cardata2_bp = Blueprint('cardata2', __name__)

status = {
    "ihumidity": 0,
    "itemperature": 0,
}

def check_limits(value, min_val, max_val, name):
    if value < min_val or value > max_val:
        return jsonify({"Error": f"{name} value {value} is out of range ({min_val} to {max_val})"}), 400
    return None

@cardata2_bp.route('/ihumidity/post', methods=['POST'])
def ihumidity_post():
    ihumidity = request.json["ihumidity"]
    error = check_limits(ihumidity, 0, 100, "ihumidity")
    if error:
        return error
    status["ihumidity"] = ihumidity
    return jsonify({"ihumidity": status["ihumidity"]})

@cardata2_bp.route('/ihumidity/get', methods=['GET'])
def ihumidity_get():
    return jsonify({"ihumidity": status["ihumidity"]})

@cardata2_bp.route('/itemperature/post', methods=['POST'])
def itemperature_post():
    itemperature = request.json["itemperature"]
    error = check_limits(itemperature, 0, 100, "itemperature")
    if error:
        return error
    status["itemperature"] = itemperature
    return jsonify({"itemperature": status["itemperature"]})

@cardata2_bp.route('/itemperature/get', methods=['GET'])
def itemperature_get():
    return jsonify({"itemperature": status["itemperature"]})
