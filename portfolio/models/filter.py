__author__ = 'Xuefeng Zhu'
from portfolio.models import db


class Filter(db.Document):
    red_flag_word = db.StringField(required=True, unique=True)
    replacement = db.StringField(required=True)
