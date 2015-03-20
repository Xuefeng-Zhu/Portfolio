__author__ = 'Xuefeng Zhu'

import os
import xmltodict
from collections import OrderedDict
from portfolio.models.project import Project
from portfolio.models.file import File
from portfolio.models.log import Log


def parse_svn_list():
    """
    Parse the svn_list.xml file into a projects
    :return project_dict
    """
    project_dict = OrderedDict()
    file_path = os.path.join(os.path.dirname(__file__),
                             'data/svn_list.xml')
    with open(file_path) as f:
        data = xmltodict.parse(f)

    entries = data["lists"]["list"]["entry"]
    for item in entries:
        if item["@kind"] == "dir":
            name = item["name"].split("/")
            if len(name) == 1:
                project_dict[name[0]] = Project(item)
        elif item["@kind"] == "file":
            file = File(item)
            project_name = item["name"].split("/")[0]
            project_dict[project_name].add_file(file)

    return project_dict


def parse_svn_log(project_dict=None):
    """
    Parse the svn_log.xml file into a logs
    :param project_dict: projects used to associate with logs
    :return: log_dict
    """
    log_dict = OrderedDict()
    file_path = os.path.join(os.path.dirname(__file__),
                             'data/svn_log.xml')
    with open(file_path) as f:
        data = xmltodict.parse(f)

    logs = data["log"]["logentry"]

    for log in logs:
        log_dict[log["@revision"]] = Log(log)
        if project_dict is not None:
            assign_file_revision(project_dict, log)
    return log_dict


def assign_file_revision(project_dict, log):
    """
    Assign revision to the files associated with it
    :param project_dict:
    :param log:
    """
    paths = log["paths"]["path"]
    if not isinstance(paths, list):
        paths = [paths]
    for item in paths:
        if item["@kind"] == "file":
            file_path = item["#text"].split("/")
            project = project_dict[file_path[2]]
            file_revision_list = project.file_dict.setdefault("/".join(file_path[2:]), [])
            if log["@revision"] not in file_revision_list:
                file_revision_list.append(log["@revision"])


