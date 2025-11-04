import csv
from config import db
from models import Brand, Bottle, Review

def upload_brands():
    with open('/home/zherevchuk-da/Документы/Двфу/web/practice/app/data/japanese_whisky_review.csv') as f:
        reader = csv.reader(f)
        next(reader)

        brands = set()
        for item in reader:
            brand_name = item[2].strip()
            if brand_name not in brands:
                brands.add(brand_name)
                new_brand = Brand(name=brand_name)
                db.session.add(new_brand)
        db.session.commit()




def upload_bottles():
    with open('/home/zherevchuk-da/Документы/Двфу/web/practice/app/data/japanese_whisky_review.csv') as f:
        reader = csv.reader(f)
        next(reader)

        bottles = set()
        for item in reader:
            bottle_name = item[1]
            brand_name = item[2]

            brand = Brand.query.filter_by(name=brand_name).first()

            key = (bottle_name, brand.id)
            if key not in bottles:
                bottles.add(key)
                new_bottle = Bottle(name=bottle_name, brand_id=brand.id)
                db.session.add(new_bottle)
        db.session.commit()


def upload_reviews():
    with open('/home/zherevchuk-da/Документы/Двфу/web/practice/app/data/japanese_whisky_review.csv') as f:
        reader = csv.reader(f)
        next(reader)

        for item in reader:
            bottle_name = item[1].strip()
            title = item[3].strip()
            content = item[4].strip()


            bottle = Bottle.query.filter_by(name=bottle_name).first()

            if bottle:
                review = Review(bottle_id=bottle.id, title=title, content=content)
                db.session.add(review)

        db.session.commit()

# upload_brands()
# upload_bottles()
# upload_reviews()