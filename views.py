from flask import Blueprint, render_template, request, jsonify

views = Blueprint(__name__, "views")

# home page
@views.route("/")
def home():
    return render_template("index.html", name="andre", age=21)

# query parameters
@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name=name)

# return json data
@views.route("/json")
def get_json():
    return jsonify({'name': 'andre', 'coolness': 10})

