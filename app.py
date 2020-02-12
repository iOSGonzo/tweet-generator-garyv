from flask import Flask
import requests
from histogram import sample
app = Flask(__name__)


@app.route('/')
def hello():
    random_word = sample("words.txt")

    return random_word

if __name__ == '__main__':
    app.run()
