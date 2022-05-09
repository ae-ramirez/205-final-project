from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap
import requests
import json

app = Flask(__name__)
bootstrap = Bootstrap(app)

OMDB_API_URL = 'http://www.omdbapi.com/'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search_page():
    # return search page
    if request.method == 'GET':
        return render_template('search.html')

    # return search results
    api_key = "b9a0cb14"
    title = request.form['query']
    params = {'apikey': api_key, 's': title}
    data = fetch_data(OMDB_API_URL, params)
    print(data)
    return render_template('search.html', results=data['Search'])

# get json data from site and return it
# param:    url: url to get response from
# return:   returns the api response as a dictionary
def fetch_data(url, parameters):
    response = requests.get(url, params=parameters)
    return response.json()
