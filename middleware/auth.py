from functools import wraps
from flask import request, jsonify
import jwt
from app import app, db
from models import student_model  # import your Student model

# Token required decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # JWT token sent in headers
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            # Decode token
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_student = student_model.query.filter_by(id=data['student_id']).first()
        except Exception as e:
            return jsonify({'message': 'Token is invalid!', 'error': str(e)}), 401

        # Inject current_student into the route
        return f(current_student, *args, **kwargs)

    return decorated
