__author__ = 'Xuefeng Zhu'
from flask import render_template, current_app, Blueprint, request, jsonify

project = Blueprint("project", __name__)


@project.route("/")
def index():
    """
    Render the project list page
    """
    return render_template("index.html",
                           project_dict=current_app.config["project_dict"],
                           log_dict=current_app.config["log_dict"])


@project.route("/<project_title>")
def project_detail(project_title):
    """
    Render the project detail page
    :param project_title: The specific project trying to view
    """
    project = current_app.config["project_dict"][project_title]
    project.file_list.sort(key=lambda file: int(file.revision))

    return render_template("project_detail.html",
                           project=project,
                           log_dict=current_app.config["log_dict"])


@project.route("/comment/<project_title>", methods=["GET", "POST"])
def project_comment(project_title):
    if request.method == "GET":
        return get_comments(project_title)
    elif request.method == "POST":
        return post_comment()
    else:
        return "Illegal"


def get_comments(project_title):
    return project_title


def post_comment():
    return jsonify(request.json)



