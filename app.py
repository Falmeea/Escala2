from flask import Flask, render_template, redirect, url_for
from views import landing
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
from flask_frozen import Freezer

app = Flask(__name__)
app.register_blueprint(landing, url_prefix="/")

app = Flask(__name__)
mailchimp = MailchimpMarketing.Client()
mailchimp.set_config({
    "api_key": "c9b7cef64f1dcdf312c9f401e9518313-us18",
    "server": "-us18"  # e.g., "us5" if your server is us5.api.mailchimp.com
})

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
    #(app.run(debug=True))