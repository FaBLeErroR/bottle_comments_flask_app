from config import db
from models import Brand, Bottle, Review
from sqlalchemy import func, desc, and_, asc, text

def get_all_info():
    query = (
        db.session.query(
            Brand.name.label("Бренд"),
            Bottle.name.label("Сорт"),
            Review.title.label("Заголовок"),
            Review.content.label("Отзыв")
        )
        .join(Bottle, Bottle.brand_id == Brand.id)
        .join(Review, Review.bottle_id == Bottle.id)
    )
    return query.statement.columns.keys(), query.all()

def get_title_contains_info(name):
    query = (
        db.session.query(Review.title, Review.content)
        .filter(Review.title.contains(name))
    )
    return query.statement.columns.keys(), query.all()

def get_title_ordered_info():
    query = (
        db.session.query(
            Review.title.label('Заголовок'),
            Review.content.label('Отзыв'),
            Bottle.name.label('Сорт')
        )
        .join(Bottle, Review.bottle_id == Bottle.id)
        .order_by(func.lower(Review.title))
    )
    return query.statement.columns.keys(), query.all()


def get_brand_review_quantity():
    query = (
        db.session.query(
            Brand.name.label("Бренд"),
            func.count(Review.id).label("Кол-во отзывов")
        )
        .join(Bottle, Bottle.brand_id == Brand.id)
        .join(Review, Review.bottle_id == Bottle.id)
        .group_by(Brand.id)
        .order_by(desc("Кол-во отзывов"))
    )
    return query.statement.columns.keys(), query.all()

def get_bottle_review_quantity():
    query = (
        db.session.query(
            Bottle.name.label("Сорт"),
            func.count(Review.id).label("Кол-во отзывов")
        )
        .join(Review, Review.bottle_id == Bottle.id)
        .group_by(Bottle.id)
        .having(and_(func.count(Review.id) > 10, func.count(Review.id) < 30))
        .order_by(desc("Кол-во отзывов"))
    )
    return query.statement.columns.keys(), query.all()


