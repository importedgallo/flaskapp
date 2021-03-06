from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

# home page
@views.route("/")
def home():
    return render_template("index.html", name="andre", age=21)

# render profile.html
@views.route("/profile")
def profile():
    return render_template("profile.html")

# return json data
@views.route("/json")
def get_json():
    return jsonify({'name': 'andre', 'coolness': 10})

# get json data
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

#redirect to a different page
@views.route("/go-to-home")
def got_to_home():
    return redirect(url_for("views.home"))
    