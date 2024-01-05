"""Write a function filter_long_words()that takes a list of words and an integer nand returns the list of
words that are longer than n.
"""



def filter_long_words(list , n):
   return [words for words in list if len(words) > n]
print(filter_long_words(['Hello', 'world', 'Haiti', 'Pythonistas!'], 8))
print(filter_long_words(['Python', 'stole', 'my', 'heart'], 5))
print(filter_long_words(['This', 'will', 'be', 'cool'], 4))






