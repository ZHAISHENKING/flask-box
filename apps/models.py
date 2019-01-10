from admin import db


class Demo(db.Document):
    """
    demo
    """
    name = db.StringField()
    both = db.IntField()
    # create_at = db.DateTimeField()
