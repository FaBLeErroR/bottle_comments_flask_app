from app.extensions import db

class Bottle(db.Model):
    __tablename__ = 'bottles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'), nullable=False)
    brand = db.relationship('Brand', back_populates='bottles')
    reviews = db.relationship('Review', back_populates='bottle', cascade='all,delete', lazy='select')
    # reviews = db.relationship('Review', back_populates='bottle', cascade='all,delete-orphan')

    def __init__(self, name, brand_id):
        self.name = name
        self.brand_id = brand_id

    def __repr__(self):
        return f'\nid: {self.id}, Название: {self.name}, Брэнд: {self.brand}'
    