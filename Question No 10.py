"""Define a function overlapping()that takes two lists and returns True if they have at least one member in
common, False otherwise. You may use your is_member()function, or the inoperator, but for the sake
of the exercise, you should (also) write it using two nested for­loops.
"""


def overlapping_two_list(list1,list2):
    for element1 in list1:
        for element2 in list2:
            if element1 == element2:
                return True
            else:
                False
                
print(overlapping_two_list([1,2,3,4,4,5,6],[2,7,8,9,0]))