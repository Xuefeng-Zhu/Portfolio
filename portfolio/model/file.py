__author__ = 'Xuefeng Zhu'
from datetime import datetime


class File:
    def __init__(self, entry_dict):
        self.path = entry_dict["name"]
        self.size = entry_dict["size"]
        commit_dict= entry_dict["commit"]
        self.revision = commit_dict["@revision"]
        self.author = commit_dict["author"]
        self.date = datetime.strptime(commit_dict["date"],
                                      "%Y-%m-%dT%H:%M:%S.%fZ")