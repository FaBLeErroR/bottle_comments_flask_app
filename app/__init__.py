from flask import Flask
from .extensions import db
from .config import DevelopmentConfig
from app.models import Brand, Bottle, Review

# Импортируем маршруты
from .routes import title, brand, review

def create_app():
    app = Flask(__name__)
    app.json.ensure_ascii = False
    app.config.from_object(DevelopmentConfig)
    # Инициализация расширений
    db.init_app(app)
    # Регистрация Blueprint-ов
    app.register_blueprint(title.bp_title, url_prefix="/api/v1/title")
    app.register_blueprint(brand.bp_brand, url_prefix="/api/v1/brands")
    app.register_blueprint(review.bp_review, url_prefix="/api/v1/reviews")
    return app