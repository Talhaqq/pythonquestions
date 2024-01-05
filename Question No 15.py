"""Write a function find_longest_word()that takes a list of words and returns the length of the longest
one.
"""


def find_longest_word(word_list):
    longest = ""
    for word in word_list:
        if len(word) > len(longest):
            longest = word
            
    return len(longest)

print(find_longest_word(["Hello", "Talha qureshi", "Nice boy", "how are you"]))
            