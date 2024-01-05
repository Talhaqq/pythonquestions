"""Define a function that computes the length of a given list or string. (It is true that Python has the len()
function built in, but writing it yourself is nevertheless a good exercise.)
"""


def len_of_list(list1):
    count = 0
    for i in list1:
        count +=1
    return count

print("lenght of list is" ,len_of_list([1,2,3,4,5,6,7,5,5,4,4,3,]))

    