from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract query term from url
    query = request.args.get('query')

    # TODO: Make 'params' dict with query term and API key
    params = {
        "api": "566RIQJP8K3Q",
        "query": query
    }

    # TODO: Make an API call to Tenor using the 'requests' library
    r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (params["query"], params["api"], 10))

    if not r.status_code == 200:
        print("error")

    # TODO: Get the first 10 results from the search results
    top10gifs = json.loads(r.content)

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter

    return render_template("index.html", gif = top10gifs)


if __name__ == '__main__':
    app.run(debug=True)
