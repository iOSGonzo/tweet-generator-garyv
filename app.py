from flask import Flask
import requests
from histogram import sample, histogram
app = Flask(__name__)


@app.route('/')
def hello():
    sentence = ""
    histogram = histogram("word.txt")
    iterations = request.args.get('iterations')
    for i in range(0, int(interations)):
        word = sample(histogram)
        sentence += word + " "
    return sentence


if __name__ == '__main__':
    app.run()
