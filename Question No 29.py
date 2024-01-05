"""Using the higher order function filter(), define a function filter_long_words()that takes a list of
words and an integer nand returns the list of words that are longer than n.
"""


def filter_long_words(words ,n):
    return list(filter(lambda x: len(x) > n, words))

print(filter_long_words(["talha", "Qureshi", "bad boy", "good boy"], 5))