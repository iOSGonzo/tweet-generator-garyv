from random import randint, choice

my_file = open("words.txt", "r")

animals = my_file.readlines()

print(choice(animals))
