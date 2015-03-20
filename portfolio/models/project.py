__author__ = 'Xuefeng Zhu'
from datetime import datetime


class Project:
    """
    Store the information of a project
    """
    def __init__(self, entry_dict):
        self.title = entry_dict["name"]
        commit_dict = entry_dict["commit"]
        self.date = datetime.strptime(commit_dict["date"],
                                      "%Y-%m-%dT%H:%M:%S.%fZ")
        self.revision = commit_dict["@revision"]
        self.file_list = list()
        self.file_dict = dict()

    def add_file(self, file):
        """
        Add a file into the project
        :param file:
        """
        self.file_list.append(file)
        self.file_dict[file.path] = [file.revision]
