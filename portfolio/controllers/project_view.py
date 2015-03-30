__author__ = 'Xuefeng Zhu'
from flask import render_template, current_app, Blueprint, request, jsonify, abort
from portfolio.models.comment import Comment


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
        return post_comment(project_title)
    else:
        return "Illegal"


def get_comments(project_title):
    comments = Comment.objects(project=project_title)
    return jsonify(data=comment_list_serialize(comments))


def post_comment(project_title):
    author = request.json.get("author")
    content = request.json.get("content")

    if author is None or content is None:
        abort(400)

    if request.json.get("parent") is None:
        comment = Comment(project=project_title, author=author, content=content)
        comment.save()
        return jsonify(comment_serialize(comment))
    else:
        parent_id = request.json.get("parent")
        comment = Comment(author=author, content=content)
        comment.save()
        success = Comment.objects(id=parent_id).update_one(push__children=comment)

        if success is 0:
            abort(400)

        return jsonify(comment_serialize(comment))


def comment_serialize(comment):
    return {
        "id": str(comment.id),
        "author": comment.author,
        "date": comment.date.strftime("%B %d, %Y %I:%M%p"),
        "content": comment.content,
        "children": comment_list_serialize(comment.children)
    }


def comment_list_serialize(comments):
    result = []
    for comment in comments:
        result.append(comment_serialize(comment))
    return result





