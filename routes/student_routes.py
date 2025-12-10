from flask import Blueprint, jsonify
from middleware.auth import token_required

student_bp = Blueprint('student', __name__)

@student_bp.route('/profile', methods=['GET'])
@token_required
def get_profile(current_student):
    return jsonify({
        'id': current_student.id,
        'name': current_student.name,
        'email': current_student.email
    })
