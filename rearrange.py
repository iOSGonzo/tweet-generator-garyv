import sys
import random

words_inputed = sys.argv[1:]
random.shuffle(words_inputed)

print(words_inputed)
