__author__ = 'Xuefeng Zhu'
from datetime import datetime
from collections import OrderedDict

class File:
    type_dict = OrderedDict({
        "code": ["java", "py"],
        "image": ["png"],
        "test": ["test"],
        "documentation": ["doc"],
        "resource": ["json", "js", "css", "xml"]
    })


    def __init__(self, entry_dict):
        self.path = entry_dict["name"]
        self.size = entry_dict["size"]
        commit_dict= entry_dict["commit"]
        self.revision = commit_dict["@revision"]
        self.author = commit_dict["author"]
        self.date = datetime.strptime(commit_dict["date"],
                                      "%Y-%m-%dT%H:%M:%S.%fZ")
        self.type = "undefined"
        self.check_type()

    def check_type(self):
        for type, list in self.type_dict.iteritems():
            for item in list:
                if item in self.path.lower():
                    self.type = type

