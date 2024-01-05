"""Define a function sum()and a function multiply()that sums and multiplies (respectively) all the
numbers in a list of numbers. For example, sum([1, 2, 3, 4])should return 10, and multiply([1,
2, 3, 4])should return 24.
"""


def sum(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number
    return total_sum



def multiply(numbers):
    total_product = 1
    for number in numbers:
        total_product *= number
        
    return total_product


print(sum([1,2,3,4]))
print(multiply([1,2,3,4]))
    
    
    

