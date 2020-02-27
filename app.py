from flask import Flask
import requests
from histogram import sample, histogram
from random import randint
from markov import MarkovChain

app = Flask(__name__)


@app.route('/')

def hello():

    hs = histogram("words.txt")
    samp = sample(hs)
    return samp


if __name__ == '__main__':
    app.run()
