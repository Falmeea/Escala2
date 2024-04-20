from flask import Flask, render_template
from views import landing
from flask_frozen import Freezer

app = Flask(__name__)
app.register_blueprint(landing, url_prefix="/")

app.config['FREEZER_RELATIVE_URLS'] = True

# Define the route for the index page
# Define the route for the index page
@app.route('/')
def index():
    return render_template('index.html')

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
    
    freezer.freeze()
