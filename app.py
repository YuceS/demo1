
from flask import Flask
from flask import request


app = Flask(__name__)




@app.before_request
def log_request():
    app.logger.debug("Request Headers %s", request.headers)
    return None


@app.route("/")
def hello():
    return "Hello BARIS! " + ", ".join(request.access_route)
    #return "Hello BARIS! " + "https://circleci.com/gh/YuceS/demo1.svg?style=shield"


@app.route("/status")
def badge():
    return "<HTML><img href=\"https://circleci.com/gh/YuceS/demo1.svg?style=shield\" > </img> </HTML>"

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug='true',port='9999')
