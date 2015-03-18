__author__ = 'Xuefeng Zhu'
from flask.ext.assets import Bundle


bundles = {
    "main_js": Bundle(
        "js/jquery-1.10.1.min.js",
        "js/bootstrap.min.js",
        output="public/js/main.js",
    ),
    "main_css": Bundle(
        "css/bootflat.min.css",
        output="public/css/main.css",
    )

}