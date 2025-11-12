from flask import Blueprint, jsonify, request
from app.models.review import Review
from app.extensions import db, auth
from app.schemas.review import review_schema, reviews_schema
from marshmallow import ValidationError

bp_review = Blueprint('review', __name__)

# curl -u student:dvfu -i http://localhost:5000/api/v1/reviews/
@bp_review.route('/', methods=['GET'])
@auth.login_required
def get_reviews():
    reviews = Review.query.all()
    return jsonify({
        "success": True,
        "reviews": reviews_schema.dump(reviews)
    }), 200

# curl -u student:dvfu -i http://localhost:5000/api/v1/reviews/1
@bp_review.route('/<int:id>', methods=['GET'])
@auth.login_required
def get_review(id):
    review = Review.query.get(id)
    if not review:
        return jsonify({
        "success": False,
        "error": "Review not found"
        }), 404
    
    return jsonify({
        "success": True,
        "reviews": review_schema.dump(review)
    }), 200

# curl -u student:dvfu -i -H "Content-Type: application/json" \
#     -X POST http://localhost:5000/api/v1/reviews/ \
#     -d '{
#         "title": "Заголовок",
#         "content": "Отзыв",
#         "bottle_id": 1
#     }'
@bp_review.route('/', methods=['POST'])
@auth.login_required
def add_review():
    try:
        data = request.get_json()
        validated_data = review_schema.load(data, session=db.session)

        review = Review(
            title=validated_data['title'],
            content=validated_data['content'],
            bottle_id=validated_data['bottle_id']
        )
        
        db.session.add(review)
        db.session.commit()
        return jsonify({
            "success": True,
            "reviews": review_schema.dump(review)
        }), 201
    
    except ValidationError as err:
        db.session.rollback()
        return jsonify({
            "success": False,
            "errors": err.messages
        }), 400
    
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
    
# curl -u student:dvfu -i -H "Content-Type: application/json" \
#     -X PUT http://localhost:5000/api/v1/reviews/1126 \
#     -d '{
#         "title": "Новый заголовок",
#         "content": "Новый отзыв."
#     }'
@bp_review.route('/<int:id>', methods=['PUT'])
@auth.login_required
def update_review(id):
    try:
        review = Review.query.get(id)
        if not review:
            return jsonify({
                "success": False,
                "error": "Review not found"
            }), 404

        data = request.get_json()
        validated_data = review_schema.load(data, session=db.session, partial=True)

        if 'title' in validated_data:
            review.title = validated_data['title']
        if 'content' in validated_data:
            review.content = validated_data['content']
        if 'bottle_id' in validated_data:
            review.bottle_id = validated_data['bottle_id']

        db.session.commit()
        return jsonify({
            "success": True,
            "reviews": review_schema.dump(review)
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
    
# curl -u student:dvfu -i -X DELETE http://localhost:5000/api/v1/reviews/1126
@bp_review.route('/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_review(id):
    try:
        review = Review.query.get(id)
        if not review:
            return jsonify({
                "success": False,
                "error": "Review not found"
            }), 404

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
    