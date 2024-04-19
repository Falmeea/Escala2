from flask import Flask, render_template
from views import landing
from flask_frozen import Freezer

app = Flask(__name__)
app.register_blueprint(landing, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return 'Hello, this is my Flask app converted to a static site!'

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()