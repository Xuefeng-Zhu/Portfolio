__author__ = 'Xuefeng Zhu'

from flask import Flask
import portfolio.utils.parser as parser
from portfolio.controllers.project_view import project

app = Flask(__name__)
app.config["project_dict"] = parser.parse_svn_list()
app.config["log_dict"] = parser.parse_svn_log()

app.register_blueprint(project)

app.run(debug=True)


