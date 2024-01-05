"""Define a function max_of_three()that takes three numbers as arguments and returns the largest of
them.
"""


def max_of_three(num1 , num2 ,num3):
    if num1 > num2 and num1 > num3:
        print("num1 is largest", num1)
        
    elif num2 > num3 and num2 > num1:
        print("NUm2 is largest", num2)
        
    else:
        print("num3 is largest", num3)
        
max_of_three(30 , 29, 28)