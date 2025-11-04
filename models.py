from config import db
from app import app

class Brand(db.Model):
    __tablename__ = 'brands'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    bottles = db.relationship('Bottle', back_populates='brand', cascade='all,delete')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'\nid: {self.id}, Название: {self.name}'


class Bottle(db.Model):
    __tablename__ = 'bottles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'), nullable=False)
    brand = db.relationship('Brand', back_populates='bottles')
    reviews = db.relationship('Review', back_populates='bottle', cascade='all,delete')
    # reviews = db.relationship('Review', back_populates='bottle', cascade='all,delete-orphan')

    def __init__(self, name, brand_id):
        self.name = name
        self.brand_id = brand_id

    def __repr__(self):
        return f'\nid: {self.id}, Название: {self.name}, Брэнд: {self.brand}'

    


class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    bottle_id = db.Column(db.Integer, db.ForeignKey('bottles.id'), nullable=False)
    title = db.Column(db.String)
    content = db.Column(db.Text, nullable=False)
    bottle = db.relationship('Bottle', back_populates='reviews')

    def __init__(self, bottle_id, title, content):
        self.bottle_id = bottle_id
        self.title = title
        self.content = content

    def __repr__(self):
        return f'\nid: {self.id}, Сорт: {self.bottle}, Тайтл: {self.title}, Отзыв: {self.co}'




app.app_context().push()
with app.app_context():
    db.create_all()