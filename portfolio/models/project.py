__author__ = 'Xuefeng Zhu'
from datetime import datetime


class Project:
    def __init__(self, entry_dict):
        self.title = entry_dict["name"]
        commit_dict = entry_dict["commit"]
        self.date = datetime.strptime(commit_dict["date"],
                                      "%Y-%m-%dT%H:%M:%S.%fZ")
        self.revision = commit_dict["@revision"]
        self.file_list = []
