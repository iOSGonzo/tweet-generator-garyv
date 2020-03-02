from flask import Flask
import requests
from histogram import sample, histogram
from random import randint
from markov import MarkovChain

app = Flask(__name__)


@app.route('/')

def hello():

    # hs = histogram("words.txt")
    # samp = sample(hs)
    my_file = open("./words.txt", "r")
    lines = my_file.readlines()

    word_list = []

    for line in lines:
        for word in line.split():
            word_list.append(word)

    print(word_list)
    markovchain = MarkovChain(word_list)
    # return samp
    # num_words = 10

    return(markovchain.walk(10))

if __name__ == '__main__':
    app.run()
