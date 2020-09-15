from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging


app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route("/test")
def test():
    html = f"<h3>TEEEEEEST</h3>"
    return html.format(format)


@app.route("/")
def home():
    html = f"<h3>Miiiiiiiiiii</h3>"
    return html.format(format)

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=80, debug=True) 
