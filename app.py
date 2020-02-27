from flask import Flask
import requests
from histogram import sample, histogram
from random import randint
from markov import MarkovChain

app = Flask(__name__)


@app.route('/')

def hello():
    file = open('./words.txt')
    text = file.read().split()
    chain = MarkovChain(text)
    sentence = chain.walk(20) + '.'
    return sentence
    # sentence = ""
    # iterations = request.args.get('iterations')
    # for i in range(0, int(iterations)):
    #     word = sample(hs)
    #     sentence += word + ""
    # return sentence


if __name__ == '__main__':
    app.run()
