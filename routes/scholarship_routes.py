# inside routes/scholarship_routes.py (or new file routes/scholarship_recommend.py)
from flask import Blueprint, request, jsonify
from middleware.auth import token_required
from utils.recommender import recommend_for_student

scholarship_bp = Blueprint("scholarship", __name__)

# existing routes ...
# RECOMMENDATIONS (protected)
@scholarship_bp.route("/recommend", methods=["GET"])
@token_required
def recommend(current_user):
    # current_user is the student dict from middleware
    student_id = current_user.get("student_id")
    limit = int(request.args.get("limit", 10))
    recs = recommend_for_student(student_id, limit=limit)
    return jsonify({"status": True, "recommendations": recs}), 200
