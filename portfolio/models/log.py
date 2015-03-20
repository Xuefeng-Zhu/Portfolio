__author__ = 'Xuefeng Zhu'
from datetime import datetime


class Log:
    """
    Store the information of a log
    """
    def __init__(self, log_dict):
        self.revision = log_dict["@revision"]
        self.author = log_dict["author"]
        self.date = self.date = datetime.strptime(log_dict["date"],
                                                  "%Y-%m-%dT%H:%M:%S.%fZ")
        self.msg = log_dict["msg"]
