from flask import Blueprint, jsonify, request

cardata3_bp = Blueprint('cardata3', __name__)

status = {
    "CAN1Stat": "Active",
    "CAN2Stat": "Active",
    "CAN3Stat": "Active",
    "Internet": "Active",
    "Ethernet": "Active"
}

@cardata3_bp.route('/can/<num>/stat/post', methods=['POST'])
def can_stat_post(num):
    if num in ["1", "2", "3"]:
        status[f"CAN{num}Stat"] = request.json["Status"]
        return jsonify({f"CAN{num}Stat": status[f"CAN{num}Stat"]})
    else:
        return jsonify({"Error": "Invalid CAN number"}), 400

@cardata3_bp.route('/can/<num>/stat/get', methods=['GET'])
def can_stat_get(num):
    if num in ["1", "2", "3"]:
        return jsonify({f"CAN{num}Stat": status[f"CAN{num}Stat"]})
    else:
        return jsonify({"Error": "Invalid CAN number"}), 400

@cardata3_bp.route('/internet/post', methods=['POST'])
def internet_post():
    status["Internet"] = request.json["Internet"]
    return jsonify({"Internet": status["Internet"]})

@cardata3_bp.route('/internet/get', methods=['GET'])
def internet_get():
    return jsonify({"Internet": status["Internet"]})

@cardata3_bp.route('/ethernet/post', methods=['POST'])
def ethernet_post():
    status["Ethernet"] = request.json["Ethernet"]
    return jsonify({"Ethernet": status["Ethernet"]})

@cardata3_bp.route('/ethernet/get', methods=['GET'])
def ethernet_get():
    return jsonify({"Ethernet": status["Ethernet"]})
