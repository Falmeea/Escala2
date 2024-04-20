from flask import Blueprint, render_template

landing = Blueprint("landing", __name__)

@landing.route("/")
def home():
    return render_template("index.html")