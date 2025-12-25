from flask import request, jsonify
from functools import wraps
import jwt
from config import SECRET_KEY

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"error": "Admin access denied"}), 401

        try:
            token = auth_header.split(" ")[1]
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

            if payload.get("role") != "admin":
                return jsonify({"error": "Admin access denied"}), 403

            return f(payload, *args, **kwargs)

        except Exception as e:
            return jsonify({"error": "Invalid or expired token"}), 401

    return decorated
