__author__ = 'Xuefeng Zhu'
from flask import render_template, current_app, Blueprint

project = Blueprint("project", __name__)


@project.route("/")
def index():
    return render_template("index.html",
                           project_dict=current_app.config["project_dict"],
                           log_dict=current_app.config["log_dict"])


@project.route("/project/<project_title>")
def project_detail(project_title):
    project = current_app.config["project_dict"][project_title]
    project.file_list.sort(key=lambda file: int(file.revision))

    return render_template("project_detail.html",
                           project=project,
                           log_dict=current_app.config["log_dict"])


