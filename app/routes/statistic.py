from flask import Blueprint, jsonify
from sqlalchemy import func, desc
from app.schemas.statistic import all_reviews_schema, statistic_schema
from app.models.statistic import get_all_reviews, get_bottle_statistic, get_brand_statistic
from app.extensions import db, auth


statistic_bp = Blueprint('statistic', __name__)

# curl -u student:dvfu -i http://localhost:5000/api/v1/statistic/all/
@statistic_bp.route('/all/', methods=['GET'])
@auth.login_required
def all_buildings():
    results = get_all_reviews()
    return jsonify({
        "success": True,
        "all_reviews": all_reviews_schema.dump(results)
    }), 200

# curl -u student:dvfu -i http://localhost:5000/api/v1/statistic/bottles/
@statistic_bp.route('/bottles/', methods=['GET'])
@auth.login_required
def bottle_statistics():
    results = get_bottle_statistic()
    return jsonify({
        "success": True,
        "bottle_stats": statistic_schema.dump(results)
    }), 200

# curl -u student:dvfu -i http://localhost:5000/api/v1/statistic/brands/
@statistic_bp.route('/brands/', methods=['GET'])
@auth.login_required
def brand_statistics():
    results = get_brand_statistic()
    return jsonify({
        "success": True,
        "brand_stats": statistic_schema.dump(results)
    }), 200
