__author__ = 'Xuefeng Zhu'

from flask import Flask
from flask.ext.assets import Environment
from portfolio.assets import bundles
import portfolio.utils.parser as parser
from portfolio.controllers.project_view import project


app = Flask(__name__)
app.config["project_dict"] = parser.parse_svn_list()
app.config["log_dict"] = parser.parse_svn_log()

assets = Environment(app)
assets.register(bundles)

app.register_blueprint(project)

if __name__ == "__main__":
    app.run(debug=True)