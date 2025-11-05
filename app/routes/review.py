from flask import Blueprint, jsonify, request
from app.models.review import Review
from app.extensions import db, auth

bp_review = Blueprint('review', __name__)


@bp_review.route('/', methods=['GET'])
@auth.login_required
def get_reviews():
    reviews = Review.query.all()
    return jsonify({
        "success": True,
        "reviews": str(reviews)
    }), 200

@bp_review.route('/<int:id>', methods=['GET'])
def get_review(id):
    review = Review.query.get(id)
    return jsonify({
        "success": True,
        "reviews": str(review)
    }), 200

@bp_review.route('/', methods=['POST'])
def add_review():
    try:
        validated_data = request.get_json()

        review = Review(
            title=validated_data['title'],
            content=validated_data['content'],
            bottle_id=validated_data['bottle_id']
        )
        
        db.session.add(review)
        db.session.commit()
        return jsonify({
            "success": True,
            "reviews": str(review)
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
    
@bp_review.route('/<int:id>', methods=['PUT'])
def update_review(id):
    try:
        review = Review.query.get(id)

        validated_data = request.get_json()
        if 'title' in validated_data:
            review.title = validated_data['title']
        if 'content' in validated_data:
            review.content = validated_data['content']
        if 'bottle_id' in validated_data:
            review.bottle_id = validated_data['bottle_id']

        db.session.commit()
        return jsonify({
            "success": True,
            "reviews": str(review)
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
    
@bp_review.route('/<int:id>', methods=['DELETE'])
def delete_review(id):
    try:
        review = Review.query.get(id)

        db.session.delete(review)
        db.session.commit()
        return jsonify({
            "success": True,
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500