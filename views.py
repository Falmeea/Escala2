from flask import Blueprint, render_template

landing = Blueprint("landing", __name__)

@landing.route("/")
def home():
    return render_template("landing.html")

# Route for the second page (Homepage)
@landing.route("/home")
def homepage():
    return render_template("homepage.html")