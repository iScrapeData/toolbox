from flask import Flask, render_template, request
from .search_string import processit

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
@app.route("/index", methods=["POST", "GET"])
@app.route("/home", methods=["POST", "GET"])
def index():

    # Default
    default_search = "https://github.com/iScrapeData"

    # User input or default
    search_term = request.form.get("q", default_search)

    strip_search = processit(search_term)

    return render_template("index.html", search_term=search_term, strip_search=strip_search)