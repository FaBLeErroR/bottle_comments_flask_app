from app.models.brand import Brand
from app.extensions import ma, db

class BrandSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Brand


brand_schema = BrandSchema()
brands_schema = BrandSchema(many=True)
