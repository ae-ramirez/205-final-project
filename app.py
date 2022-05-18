"""
github:
https://github.com/ae-ramirez/205-final-project
"""

from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap
import requests
import json

app = Flask(__name__)
bootstrap = Bootstrap(app)
OMDB_API_URL = 'http://www.omdbapi.com/'
OMDB_API_KEY = 'b9a0cb14'
IMDB_API_URL = 'https://imdb-api.com/en/API/'
IMDB_API_KEY = 'k_peu1q0jh'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search_page():
    # return search page
    if request.method == 'GET':
        return render_template('search.html')

    # return search results
    title = request.form['query']
    params = {'apikey': OMDB_API_KEY, 's': title}
    data = fetch_data(OMDB_API_URL, params)
    print(data)
    return render_template('search.html', results=data['Search'])


@app.route('/movie/<imdbID>')
def movie_info(imdbID):
    # might be able to scrape the trailer using the imdb id
    # although theres probably a better way of getting the trailer
    url = IMDB_API_URL + 'Trailer/' + IMDB_API_KEY + '/' + imdbID
    data = fetch_data(url)
    print(data)
    url2= IMDB_API_URL + 'Ratings/' + IMDB_API_KEY + '/' + imdbID
    data2=fetch_data(url2)
    print(data2)
    # params = {'apikey': OMDB_API_KEY, 'i':imdbID}
    # data3 = fetch_data(OMDB_API_URL, params)

    return render_template('movie.html', movie_info={"t":data, "r":data2})


# get json data from site and return it
# param:    url: url to get response from
# return:   returns the api response as a dictionary
def fetch_data(url, parameters=""):
    response = requests.get(url, params=parameters)
    return response.json()
