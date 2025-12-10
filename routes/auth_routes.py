from flask import Blueprint, request, jsonify
from models.student_model import StudentModel
from config import SECRET_KEY
import bcrypt
import jwt
import datetime

auth = Blueprint("auth", __name__)

# REGISTER
@auth.route("/register", methods=["POST"])
def register():
    data = request.json
    StudentModel.create_student(data)
    return jsonify({"message": "Registration successful!"})


# LOGIN
@auth.route("/login", methods=["POST"])
def login():
    data = request.json
    user = StudentModel.get_student_by_email(data["email"])

    if not user:
        return jsonify({"error": "Email not found"}), 404

    if not bcrypt.checkpw(data["password"].encode(), user["password"].encode()):
        return jsonify({"error": "Incorrect password"}), 401

    token = jwt.encode({
        "id": user["id"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=6)
    }, SECRET_KEY, algorithm="HS256")

    return jsonify({"message": "Login successful", "token": token})
