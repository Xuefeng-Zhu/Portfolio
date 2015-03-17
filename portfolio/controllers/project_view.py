__author__ = 'Xuefeng Zhu'
from flask import render_template, current_app, Blueprint

project = Blueprint("project", __name__)


@project.route("/")
def index():
    return render_template("index.html", project_dict=current_app.config["project_dict"])


