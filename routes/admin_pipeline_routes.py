from flask import Blueprint, jsonify
from pipeline.pipeline_runner import run_pipeline
from middleware.admin_auth import admin_required

admin_pipeline_bp = Blueprint("admin_pipeline", __name__)

@admin_pipeline_bp.route("/pipeline/run", methods=["POST"])
@admin_required
def run_scholarship_pipeline():
    result = run_pipeline()
    return jsonify(result)
