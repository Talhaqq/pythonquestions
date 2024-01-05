"""Write a program that maps a list of words into a list of integers representing the lengths of the correponding
words.
"""

def list_of_words(list1):
    new_list = [len(i) for i in list1]
    return new_list

print(list_of_words(["hello", "talha qureshi", "good boy", "bad boy"]))