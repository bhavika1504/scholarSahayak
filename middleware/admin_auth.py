from flask import request, jsonify
from functools import wraps
from config import ADMIN_TOKEN

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("X-ADMIN-TOKEN")

        if not token or token != ADMIN_TOKEN:
            return jsonify({"error": "Admin access denied"}), 403

        return f(*args, **kwargs)
    return decorated
