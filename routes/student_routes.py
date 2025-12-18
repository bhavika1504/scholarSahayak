from flask import Blueprint, jsonify, request
from middleware.auth import token_required
from models.student_model import StudentModel
from utils.recommender import recommend_for_student

student_bp = Blueprint("student", __name__)

# --------- GET PROFILE ---------
@student_bp.route("/profile", methods=["GET"])
@token_required
def get_profile(current_student):

    student_data = StudentModel.get_student_by_id(
        current_student["student_id"]   # ✅ positional argument
    )

    if not student_data:
        return jsonify({"error": "Student not found"}), 404

    student_data.pop("password", None)

    return jsonify(student_data), 200

# --------- UPDATE PROFILE ---------
@student_bp.route("/profile", methods=["PUT"])
@token_required
def update_profile(current_student):

    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    result = StudentModel.update_student(
        current_student["student_id"],
        data
    )

    if not result["status"]:
        return jsonify(result), 400

    # fetch updated profile
    updated_student = StudentModel.get_student_by_id(
        current_student["student_id"]
    )
    updated_student.pop("password", None)

    return jsonify({
        "status": True,
        "message": "Profile updated successfully",
        "student": updated_student
    }), 200

# --------- GET RECOMMENDATIONS ---------
@student_bp.route("/recommendations", methods=["GET"])
@token_required
def get_recommendations(current_student):

    recommendations = recommend_for_student(
        current_student["student_id"],  # ✅ positional argument
        limit=10
    )

    return jsonify({
        "status": True,
        "count": len(recommendations),
        "recommendations": recommendations
    }), 200
