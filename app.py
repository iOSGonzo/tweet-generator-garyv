from flask import Flask
import requests
from histogram import sample, histogram
from random import randint
app = Flask(__name__)


@app.route('/')

def hello():
    sentence = ""
    iterations = request.args.get('iterations')
    for i in range(0, int(iterations)):
        word = sample("words.txt")
        sentence += word + ""
    return sentence


if __name__ == '__main__':
    app.run()
