__author__ = 'Xuefeng Zhu'

from portfolio.models.filter import Filter
from portfolio.app import app

filters = [("fuck", "bi"), ("damn", "bi"), ("kill", "bi"), ("asshole", "bi"),
           ("ass", "bi"), ("nude", "bi")]

if __name__ == "__main__":
    for pair in filters:
        filter = Filter(red_flag_word=pair[0], replacement=pair[1])
        try:
            filter.save()
        except:
            pass
