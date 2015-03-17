__author__ = 'Xuefeng Zhu'

import os
import xmltodict
from portfolio.models.project import Project
from portfolio.models.file import File
from portfolio.models.log import Log


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
                project_dict[name[0]] = Project(item)
        elif item["@kind"] == "file":
            file = File(item)
            project_name = item["name"].split("/")[0]
            project_dict[project_name].file_list.append(file)

    return project_dict


def parse_svn_log():
    log_dict = dict()
    file_path = os.path.join(os.path.dirname(__file__),
                             'data/svn_log.xml')
    with open(file_path) as f:
        data = xmltodict.parse(f)

    logs = data["log"]["logentry"]

    for log in logs:
        log_dict[log["@revision"]] = Log(log)

    return log_dict
