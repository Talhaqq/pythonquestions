"""Write a program that maps a list of words into a list of integers representing the lengths of the correponding
words. Write it in three different ways: 1) using a for­loop, 2) using the higher order function map(), and 3)
using list comprehensions."""


def word_length_one(words):
    wordslenght = []
    for word in words:
        wordslenght.append(len(word))
    return wordslenght
    
    
    
def word_length_two(words):
    return map(len , words)



def word_length_three(words):
    return [len(word) for word in words]

print(word_length_one(['lol', 'this', 'is', 'funny']))
print(word_length_two(['lol', 'this', 'is', 'NOT', 'funny']))
print(word_length_three(['or', 'is', 'it', '?']))

