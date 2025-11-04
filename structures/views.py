from flask import render_template, request
from config import db
from models import Brand, Bottle, Review
from sqlalchemy import func, desc
from app import app
from structures.query import (
    get_all_info,
    get_bottle_review_quantity,
    get_brand_review_quantity,
    get_title_contains_info,
    get_title_ordered_info,
)

# main = Blueprint('main', __name__)

@app.route('/')
def index():
    tab = request.args.get('tab', 1, type=int)
    page = request.args.get('page', 1, type=int)
    per_page = 10

    all_head, all_data = get_all_info()
    yazumaki_head, yazumaki_data = get_title_contains_info('Yamazaki')
    ordered_head, ordered_data = get_title_ordered_info()
    brand_quantity_head, brand_quantity_data = get_brand_review_quantity()
    bottle_quantity_head, bottle_quantity_data = get_bottle_review_quantity()

    tabs = [
        {'id': 1, 'title': 'Полная информация', 'head': all_head, 'data': all_data},
        {'id': 2, 'title': 'Фильтр (Yamazaki)', 'head': yazumaki_head, 'data': yazumaki_data},
        {'id': 3, 'title': 'Сортировка', 'head': ordered_head, 'data': ordered_data},
        {'id': 4, 'title': 'Статистика по брендам', 'head': brand_quantity_head, 'data': brand_quantity_data},
        {'id': 5, 'title': 'Бутылки (10–30 отзывов)', 'head': bottle_quantity_head, 'data': bottle_quantity_data},
    ]

    current_tab = tabs[tab - 1]

    current_head = current_tab['head']
    current_data = current_tab['data']

    # Преобразуем ORM объекты в кортежи, чтобы Jinja могла их отобразить
    current_data = [tuple(getattr(r, col) for col in current_head) for r in current_data]

    return render_template(
        "index.html",
        tabs=tabs,
        active_tab=tab,
        head=current_head,
        body=current_data
    )