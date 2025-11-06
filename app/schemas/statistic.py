from marshmallow import Schema,fields

class AllReviewsSchema(Schema):
    id = fields.Int(required=True)
    brand = fields.Str(required=True)
    bottle = fields.Str(required=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)

class StatisticSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    review_count = fields.Int(required=True)
    avg_length = fields.Float(required=True)
    min_length = fields.Float(required=True)
    max_length = fields.Float(required=True)
    
all_reviews_schema = AllReviewsSchema(many=True)
statistic_schema = StatisticSchema(many=True)
