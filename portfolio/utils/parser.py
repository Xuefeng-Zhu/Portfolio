__author__ = 'Xuefeng Zhu'

import os
import xmltodict
from portfolio.model.project import Project


def parse_svn_list():
    project_dict = dict()
    file_path = os.path.join(os.path.dirname(__file__),
                             'data/svn_list.xml')
    with open(file_path) as f:
        data = xmltodict.parse(f)

    entry = data["lists"]["list"]["entry"]
    for item in entry:
        if item["@kind"] == "dir":
            name = item["name"].split("/")
            if len(name) == 1:
                project_dict[name[0]] = Project(name[0], item["commit"])
        elif item["@kind"] == "file":

    print project_dict

parse_svn_list()