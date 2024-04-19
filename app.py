from flask import Flask, render_template
from views import landing
from flask_frozen import Freezer

app = Flask(__name__)
app.register_blueprint(landing, url_prefix="/")

# Define the route for the index page
@app.route('/')
def index():
<<<<<<< HEAD
    return render_template('index.html')
=======
    return 'Hello, this is my Flask app converted to a static site!'
>>>>>>> ae4d5b76291de8459d0ce02db6b89f71511d8460

# Define the route for the homepage
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/myservices')
def myservices():
    return render_template('myservices.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/thewriter')
def thewriter():
    return render_template('thewriter.html')

@app.route('/tienaread')
def tienaread():
    return render_template('tienaread.html')

@app.route('/tienaexplore')
def tienaexplore():
    return render_template('tienaexplore.html')

# Create an instance of Freezer
freezer = Freezer(app)

if __name__ == '__main__':
<<<<<<< HEAD
    # Choose between running the server or freezing the app based on your need
     app.run(debug=True)
    # freezer.freeze()
=======
    freezer.freeze()
>>>>>>> ae4d5b76291de8459d0ce02db6b89f71511d8460
