from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    query = request.args.get('query')


    params = {
        "key": "566RIQJP8K3Q",
        "q": query,
        "limit" : 10
    }

    r = requests.get('https://api.tenor.com/v1/search', params = params)

    if not r.status_code == 200:
        print("error")

    gifs_json = r.json()
    gifs = gifs_json["results"]

    return render_template("index.html", gifs = gifs)


if __name__ == '__main__':
    app.run(debug=True)
