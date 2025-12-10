from flask import Blueprint, request, jsonify
from models.student_model import StudentModel
from config import SECRET_KEY
from werkzeug.security import check_password_hash
import jwt
import datetime
from controllers.auth_controller import AuthController

auth = Blueprint("auth", __name__)

# ----------------------- LOGIN -----------------------
@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    # 1. Check if user exists
    user = StudentModel.get_student_by_email(data.get("email"))
    if not user:
        return jsonify({"error": "Email not found"}), 404

    # 2. Check password
    if not check_password_hash(user["password"], data.get("password")):
        return jsonify({"error": "Incorrect password"}), 401

    # 3. Generate JWT Token
    token = jwt.encode({
        "student_id": user["student_id"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=6)
    }, SECRET_KEY, algorithm="HS256")

    return jsonify({
        "message": "Login successful",
        "token": token,
        "student": {
            "student_id": user["student_id"],
            "name": user["name"],
            "email": user["email"]
        }
    }), 200


# ----------------------- REGISTER -----------------------
@auth.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    try:
        StudentModel.create_student(data)
        return jsonify({"message": "Registration successful!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
