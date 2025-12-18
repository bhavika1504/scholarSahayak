from flask import Blueprint, request, jsonify
from middleware.admin_auth import admin_required
from models.scholarship_model import ScholarshipModel

admin_bp = Blueprint("admin", __name__)

# -------- ADD SCHOLARSHIP --------
@admin_bp.route("/scholarships", methods=["POST"])
@admin_required
def add_scholarship():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    result = ScholarshipModel.create_scholarship(data)
    return jsonify(result), 201


# -------- UPDATE SCHOLARSHIP --------
@admin_bp.route("/scholarships/<int:scholarship_id>", methods=["PUT"])
@admin_required
def update_scholarship(scholarship_id):
    data = request.get_json()

    result = ScholarshipModel.update_scholarship(scholarship_id, data)
    return jsonify(result), 200


# -------- DELETE SCHOLARSHIP --------
@admin_bp.route("/scholarships/<int:scholarship_id>", methods=["DELETE"])
@admin_required
def delete_scholarship(scholarship_id):
    result = ScholarshipModel.delete_scholarship(scholarship_id)
    return jsonify(result), 200


# -------- VIEW ALL SCHOLARSHIPS (ADMIN) --------
@admin_bp.route("/scholarships", methods=["GET"])
@admin_required
def list_scholarships():
    data = ScholarshipModel.get_all_scholarships()
    return jsonify(data), 200
