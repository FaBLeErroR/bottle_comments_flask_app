from app.models.review import Review
from app.extensions import ma, db

class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Review

    load_instance = True
    sqla_session = db.session

    bottle_id = ma.auto_field()
    # bottle = ma.Nested(BottleSchema())
    bottle = ma.Nested("BottleSchema")


review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)
