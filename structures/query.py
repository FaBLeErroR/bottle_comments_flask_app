from config import db
from models import Brand, Bottle, Review
from sqlalchemy import func, desc

def get_all_info():
    query = (
        db.session.query(
            Brand.name.label("Бренд"),
            Bottle.name.label("Сорт"),
            Review.title.label("Заголовок"),
            Review.content.label("Отзыв")
        )
        .select_from(Brand)
        .join(Bottle)
        .join(Review)
    )
    return query.statement.columns.keys(), query.all()

def get_title_contains_info(name):
    query = (
        db.session.query(
            Review.title.label("Заголовок"), 
            Review.content.label("Отзыв")
        )
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
        .join(Bottle)
        .order_by(func.lower(Review.title))
    )
    return query.statement.columns.keys(), query.all()


def get_brand_review_quantity():
    query = (
        db.session.query(
            Brand.name.label("Бренд"),
            func.count(Review.id).label("Количество отзывов")
        )
        .select_from(Brand)
        .join(Bottle)
        .join(Review)
        .group_by(Brand.id)
        .order_by(desc("Количество отзывов"))
    )
    return query.statement.columns.keys(), query.all()

def get_bottle_review_quantity():
    subquery = (
        db.session.query(
            func.count(Review.id).label("Количество отзывов")
        )
        .select_from(Bottle)
        .join(Review)
        .group_by(Bottle.id)
        .order_by(desc("Количество отзывов"))
        .limit(1)
    )

    query = (
        db.session.query(
            Bottle.name.label("Сорт"),
            func.count(Review.id).label("Количество отзывов")
        )
        .select_from(Bottle)
        .join(Review)
        .group_by(Bottle.id)
        .having(func.count(Review.id) == subquery)
    )

    return query.statement.columns.keys(), query.all()


