from flask import Blueprint, jsonify, request
from app.models.brand import Brand
from app.extensions import db

bp_brand = Blueprint('brand', __name__)

@bp_brand.route('/', methods=['GET'])
def get_brands():
    brands = Brand.query.all()
    return jsonify({
        "success": True,
        "buildings": str(brands)
    }), 200

@bp_brand.route('/<int:id>', methods=['GET'])
def get_brand(id):
    brand = Brand.query.get(id)
    return jsonify({
        "success": True,
        "buildings": str(brand)
    }), 200
