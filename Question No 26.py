""" Using the higher order function reduce(), write a function max_in_list()that takes a list of numbers
and returns the largest one. Then ask yourself: why define and call a new function, when I can just as well
call the reduce()function directly?"""



def max_in_list(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max
print(max_in_list([1,3,4,7,88,0]))