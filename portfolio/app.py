__author__ = 'Xuefeng Zhu'
"""
Boostrap the web app
"""
from flask import Flask
from flask.ext.assets import Environment
from portfolio.assets import bundles
import portfolio.utils.parser as parser
from portfolio.controllers.project_view import project
from portfolio.models import db


app = Flask(__name__)
app.config["project_dict"] = parser.parse_svn_list()
app.config["log_dict"] = parser.parse_svn_log(app.config["project_dict"])
app.config["MONGODB_SETTINGS"] = {
    'db': 'portofolio',
    'host': 'ds059908.mongolab.com',
    'port': 59908,
    'username': 'portfolio',
    'password': '123123'
}

db.init_app(app)

assets = Environment(app)
assets.register(bundles)

app.register_blueprint(project)

if __name__ == "__main__":
    app.run(debug=True)