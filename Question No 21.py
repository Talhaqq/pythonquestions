"""Write a function char_freq()that takes a string and builds a frequency listing of the characters contained
in it. Represent the frequency listing as a Python dictionary. Try it with something like
char_freq("abbabcbdbabdbdbabababcbcbab")"""


def char_freq(str):
    d = {}
    for char in str:
        if char in d:
            d[char] += 1
            
        else:
            d[char] = 1
    return d
            
print(char_freq("abbabcbdbabdbdbabababcbcbab"))
            