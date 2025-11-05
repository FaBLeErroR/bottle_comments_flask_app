from app.extensions import db

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
        return f'\nid: {self.id}, Сорт: {self.bottle}, Тайтл: {self.title}, Отзыв: {self.content}'
