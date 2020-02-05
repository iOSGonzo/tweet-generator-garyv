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

    return(word_histogram)

def unique_words(histogram):
    unique_words = 0
    for word in word_histogram:
        if word_histogram[word] == 1:
            unique_words += 1
        else:
            pass

    return("Number of unique words: " + str(unique_words))

def frequency(word, histogram):
    for list in histogram:
        if word in list:
            return("The word " + word + " appears " + str(word_histogram[word]) + " times")
            return()
        else:
            pass


def list_histogram(source_text):
    filehandle = open(source_text, "r")
    lines = filehandle.readlines()

    histogram = []
    for word in lines:
        is_updated = False
        for list in histogram:
            if list[0] == word:
                list[1] += 1
                is_updated = True
        if is_updated == False:
            histogram.append([word,1])
    return histogram


def tuple_histogram(source_text):
    filehandle = open(source_text, "r")
    lines = filehandle.readlines()

    histogram = []
    amount = 0
    for word in lines:
        print(histogram)
        is_updated = False
        for tuple in histogram:
            if tuple[0] == word:
                amount = tuple[1] +1
                histogram.remove(tuple)
                histogram.append((word,amount))
                is_updated = True
        if is_updated == False:
            histogram.append((word, 1))
    return histogram



print(histogram("words.txt"))
print(unique_words(word_histogram))
print(frequency("sunset",word_histogram))
print(list_histogram("words.txt"))
