word_histogram = {}

def histogram(source_text):
    filehandle = open(source_text, "r")
    lines = filehandle.readlines()

    for word in lines:
        word = word.rstrip()
        if word in word_histogram:
            word_histogram[word] += 1
        else:
            word_histogram[word] = 1

    print(word_histogram)

def unique_words(histogram):
    unique_words = 0
    for word in word_histogram:
        if word_histogram[word] == 1:
            unique_words += 1
        else:
            pass

    print(unique_words)

    pass

def frequency(word, histogram):
    pass

histogram("words.txt")
unique_words(word_histogram)
