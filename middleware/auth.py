from functools import wraps
from flask import request, jsonify
import jwt
from config import SECRET_KEY
from models.student_model import StudentModel

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return jsonify({"error": "Token missing"}), 401

        parts = auth_header.split()
        if len(parts) != 2 or parts[0].lower() != "bearer":
            return jsonify({"error": "Invalid token format"}), 401

        token = parts[1]

        try:
            # decode JWT
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            student_id = data.get("student_id")

            # fetch student from DB
            current_user = StudentModel.get_student_by_id(student_id)
            if not current_user:
                return jsonify({"error": "User not found"}), 401

        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401
        except Exception as e:
            return jsonify({"error": "Token error", "details": str(e)}), 500

        # pass student to route
        return f(current_user=current_user, *args, **kwargs)

    return decorated
