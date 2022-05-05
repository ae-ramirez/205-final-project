from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap
import requests
import json

app = Flask(__name__)
bootstrap = Bootstrap(app)

omdb_api_url = 'http://www.omdbapi.com/'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search_page():
    if request.method == 'GET':
        return render_template('search.html')
    elif request.method == 'POST':
        api_key = "b9a0cb14"
        title = request.form['query']
        params = {'apikey': api_key, 's': title}
        data = fetch_data(omdb_api_url, params)
        print(data)
        return render_template('results.html', results=data)

# get json data from site and return it
# param:    url: url to get response from
# return:   returns the api response as a dictionary
def fetch_data(url, parameters):
    response = requests.get(url, params=parameters)
    return response.json()
