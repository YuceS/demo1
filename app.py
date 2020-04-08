
from flask import Flask
from flask import request


app = Flask(__name__)




@app.before_request
def log_request():
    app.logger.debug("Request Headers %s", request.headers)
    return None


@app.route("/")
def hello():
    #return "Hello BARIS!2222 "
    return "Hello BARIS! " + request.access_route



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug='true',port='9999')
