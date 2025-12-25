from flask import Blueprint, request, jsonify
import jwt
from config import SECRET_KEY

admin_auth_bp = Blueprint("admin_auth", __name__)

# 🔐 Admin Login (Hardcoded for now)
@admin_auth_bp.route("/login", methods=["POST"])
def admin_login():

    data = request.get_json()

    # temporary hardcoded admin
    if data.get("email") != "admin@gmail.com" or data.get("password") != "admin123":
        return jsonify({"error": "Invalid admin credentials"}), 401

    token = jwt.encode({
        "admin_id": 1,
        "email": "admin@gmail.com",
        "role": "admin"
    }, SECRET_KEY, algorithm="HS256")

    return jsonify({
        "message": "Admin login successful",
        "token": token
    }), 200
