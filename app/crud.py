from config import db
from models import Brand, Bottle, Review

def add_test_info():
    brand2 = Brand('Test brand2')
    db.session.add(brand2)
    db.session.commit()

    # item = Bottle()

def check_info():
    query = Brand.query.all()
    print(query)

def find_brand(id):
    query = Brand.query.filter(Brand.id == id).all()
    print(query)

def find_brand_filtred():
    query = (Brand.query.filter(Brand.name.like("%test%"))
    .order_by(Brand.name.desc()).all())
    print(query)

def update_brand():
    (Brand.query.filter(Brand.name == 'Test brand2')
    .update({Brand.name: "Test brand"})
    )
    db.session.commit()
    query = Brand.query.all()
    print(query)

def delite_brand():
    Brand.query.filter(Brand.id == 1).delete()
    db.session.commit()
    query = Brand.query.all()
    print(query)