from flask import Blueprint, jsonify
from middleware.admin_auth import admin_required
from models.admin_analytics_model import AdminAnalyticsModel

admin_analytics_bp = Blueprint("admin_analytics", __name__)

@admin_analytics_bp.route("/analytics/most-applied", methods=["GET"])
@admin_required
def most_applied(current_admin):
    data = AdminAnalyticsModel.most_applied_scholarships()
    return jsonify({"status": True, "data": data})


@admin_analytics_bp.route("/analytics/by-category", methods=["GET"])
@admin_required
def by_category(current_admin):
    data = AdminAnalyticsModel.applications_by_category()
    return jsonify({"status": True, "data": data})


@admin_analytics_bp.route("/analytics/by-state", methods=["GET"])
@admin_required
def by_state(current_admin):
    data = AdminAnalyticsModel.applications_by_state()
    return jsonify({"status": True, "data": data})
