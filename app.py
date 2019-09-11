from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract query term from url
    # try:
    query = request.args.get('query')


    # TODO: Make 'params' dict with query term and API key
    params = {
        "q": query,
        "key": "566RIQJP8K3Q",
        "limit" : 10
    }

    # TODO: Make an API call to Tenor using the 'requests' library
    r = requests.get('https://api.tenor.com/v1/search', params = params)

    if not r.status_code == 200:
        print("error")

    # TODO: Get the first 10 results from the search results
    gifs_json = r.json()
    gifs = gifs_json["results"]

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter
    print (gifs)

    return render_template("index.html", gifs = gifs)


if __name__ == '__main__':
    app.run(debug=True)
