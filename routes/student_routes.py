from flask import Blueprint, jsonify
from middleware.auth import token_required
from models.student_model import StudentModel

student = Blueprint("student", __name__)

# --------- GET PROFILE ---------
@student.route("/profile", methods=["GET"])
@token_required
def get_profile(current_student):

    # Get student details from DB using ID from token
    student_data = StudentModel.get_student_by_id(current_student["student_id"])

    if not student_data:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({
        "student_id": student_data["student_id"],
        "name": student_data["name"],
        "email": student_data["email"],
        "category": student_data["category"],
        "state_id": student_data["state_id"],
        "annual_income": student_data["annual_income"],
        "education_level": student_data["education_level"],
        "course": student_data["course"],
        "phone": student_data["phone"],
        "created_at": student_data["created_at"]
    }), 200
