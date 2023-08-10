import json

from flask import Flask, render_template, jsonify
from flask_cors import CORS

application = Flask(__name__)
CORS(application)


@application.route("/")
def index():
    return render_template("index.html")


@application.route("/get_projects")
def get_projects():
    with open("projects.json", encoding="utf-8") as file:
        data = json.load(file)

    return jsonify(data)


if __name__ == '__main__':
    application.run("127.0.0.1", 8080, debug=True)
