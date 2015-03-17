__author__ = 'Xuefeng Zhu'
from datetime import datetime


class Project:
    def __init__(self, title, commit_dict):
        self.title = title
        self.date = datetime.strptime(commit_dict["date"],
                                      "%Y-%m-%dT%H:%M:%S.%fZ")
        self.revision = commit_dict["@revision"]
        self.file_list = []
