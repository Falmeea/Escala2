from flask import Flask, render_template
from views import landing

app = Flask(__name__)
app.register_blueprint(landing, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True)