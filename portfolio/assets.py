__author__ = 'Xuefeng Zhu'
from flask.ext.assets import Bundle


bundles = {
    "main_js": Bundle(
        "js/bootstrap.min.js",
        "js/jquery-1.10.1.min.js",
        output="public/js/main.js",
    ),
    "main_css": Bundle(
        "css/bootflat.css",
        output="public/css/main.css",
    )

}