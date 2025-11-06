from app.models.bottle import Bottle
from app.extensions import ma, db

class BottleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Bottle
        
    brand_id = ma.auto_field()
    brand = ma.Nested("BrandSchema")



bottle_schema = BottleSchema()
bottles_schema = BottleSchema(many=True)
