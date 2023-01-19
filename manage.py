from flask import Flask, jsonify

app = Flask(__name__)

from scraper import Crawler, url

#route
@app.route("/")
def index():
    scrap = Crawler(url=url)
    data_dict: dict = {
        "message": scrap.crawling(),
    }
    return jsonify(data_dict)

if __name__ == "__main__":
    app.run(debug=True)