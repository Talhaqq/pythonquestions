"""Define a function reverse()that computes the reversal of a string. For example, reverse("I am
testing")should return the string "gnitset ma I"."""



def reverse(string):
    for char in string:
        new_string = char[::-1]
        return new_string
    
print(reverse(["I am testing"]))