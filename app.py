from flask import Flask
from flask import request


app = Flask(__name__)




@app.before_request
def log_request():
    app.logger.debug("Request Headers %s", request.headers)
    return None


@app.route("/")
def hello
