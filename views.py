from flask import Blueprint, render_template

landing = Blueprint("landing","homepage", __name__)

@landing.route("/")
def home():
    return render_template("landing.html")