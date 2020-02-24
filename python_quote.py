import random

quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")

def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]

if __name__ == '__main__':
    quote = random_python_quote()
    print(quote)



from random import randint
from sample import sample
from color import colors

#TODO: 1. Write the generate_words function here
def generate_words(histogram, num_words):
  counter = 1

  while counter <= num_words:
    print(sample(histogram))
    counter += 1

#Uncomment this to test printing 5 words
my_histogram = {"one":1, "fish":4, "two":1, "red":1, "blue":1}
generate_words(my_histogram, 5)


#TODO: 2. Make the functions in color.py into methods in the Rainbow class
class Rainbow:
  def __init__(self, colors):
    self.colors = colors


#uncomment to test
#my_rainbow = Rainbow(["orange", "green", "pink"])
#my_rainbow.add_color("red")
#my_rainbow.remove_color("orange")
#Should see green, pink, red printed
#my_rainbow.print_colors()
