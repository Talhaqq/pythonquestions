"""A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The
quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it
is a pangram or not.
"""



def is_pangram(sentence):
    sentence = sentence.lower()
    
    
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
    
    if set(sentence) >= alphabet_set:
        return True
    else:
        return False
    
print(is_pangram("The five boxing wizards jump quickly"))
print(is_pangram("Brown jars prevented the mixture from freezing too quickly"))
print(is_pangram("Six big devils from Japan quickly forgot how to waltz"))
print(is_pangram("Five or six big jet planes zoomed quickly by the tower"))
print(is_pangram("hello world"))
    