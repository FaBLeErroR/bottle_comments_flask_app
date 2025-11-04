from config import db
from models import Bottle,Brand,Review

def show_reviews():
    result = db.session.query(Review.title).all()
    print(result)

def show_reviews_filtered():
    result = db.session.query(Review.title, Review.content, Review.bottle).filter(Review.title.contains('Hibiki')).all()
    print(result)

def show_reviews_ordered():
    result = db.session.query(
        Review.title.label('Тайтл'), 
        Review.content.label('Отзыв'), 
        Review.bottle.label('Название')
    ).order_by('Тайтл', Review.title.desc()).all()
    print(result)

def show_all():
    result = (
    db.session.query(
        Brand.name.label("Бренд"),
        Bottle.name.label("Бутылка"),
        Review.title.label("Заголовок"),
        Review.content.label("Отзыв")
    ).join(Bottle, Bottle.brand_id == Brand.id).join(Review, Review.bottle_id == Bottle.id).all())

    print(result)

show_all()

