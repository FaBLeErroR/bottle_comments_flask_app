from app.models.review import Review
from app.models.bottle import Bottle
from app.models.brand import Brand
from sqlalchemy import func, desc
from app.extensions import db

def get_all_reviews():
    query = (
        db.session.query(
            Review.id,
            Brand.name.label("brand"),
            Bottle.name.label("bottle"),
            Review.title,
            Review.content
        )
        .join(Bottle, Bottle.id == Review.bottle_id)
        .join(Brand, Brand.id == Bottle.brand_id)
        .order_by(Brand.name, Bottle.name)
    )
    results = query.all()
    keys = query.statement.columns.keys()

    formatted_results = [
        {field_name: value for field_name, value in zip(keys, result)}
        for result in results
    ]
    return formatted_results


def get_bottle_statistic():
    query = (
        db.session.query(
            Bottle.id.label("id"),
            Bottle.name.label("name"),
            func.count(Review.id).label("review_count"),
            func.avg(func.length(Review.content)).label("avg_length"),
            func.min(func.length(Review.content)).label("min_length"),
            func.max(func.length(Review.content)).label("max_length")
        )
        .join(Review, Review.bottle_id == Bottle.id)
        .group_by(Bottle.id)
        .order_by(func.count(Review.id).desc())
    )
    results = query.all()
    keys = query.statement.columns.keys()

    formatted_results = [
        {field_name: value for field_name, value in zip(keys, result)}
        for result in results
    ]

    return formatted_results

def get_brand_statistic():
    query = (
        db.session.query(
            Brand.id.label("id"),
            Brand.name.label("name"),
            func.count(Review.id).label("review_count"),
            func.avg(func.length(Review.content)).label("avg_length"),
            func.min(func.length(Review.content)).label("min_length"),
            func.max(func.length(Review.content)).label("max_length")
        )
        .join(Bottle, Bottle.brand_id == Brand.id)
        .join(Review, Review.bottle_id == Bottle.id)
        .group_by(Brand.id)
        .order_by(func.count(Review.id).desc())
    )
    results = query.all()
    keys = query.statement.columns.keys()

    formatted_results = [
        {field_name: value for field_name, value in zip(keys, result)}
        for result in results
    ]
    
    return formatted_results

