__author__ = 'Xuefeng Zhu'
from portfolio.models import db
from datetime import datetime


class Comment(db.Document):
    """
    Store the comment information
    """
    project = db.StringField()
    author = db.StringField(required=True)
    content = db.StringField(required=True)
    date = db.DateTimeField(default=datetime.now)
    children = db.ListField(db.ReferenceField('Comment'))