import random
import sys

word_file = open("/usr/share/dict/words", "r")

lines = word_file.readlines()
num_of_words = int(sys.argv[1])

for i in range(num_of_words):
    rand_int = random.randint(0, len(lines)-1)
    print(lines[rand_int])
