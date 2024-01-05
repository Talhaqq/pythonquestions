"""Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and
returns Trueif x is a member of a, False otherwise. (Note that this is exactly what the in operator does,
but for the sake of the exercise you should pretend Python did not have this operator.)
"""

        
 
def is_mumber(value , my_list):
    for element in my_list:
        if element == value:
            return True
        
    return False
        
my_list = ["a", "b", "c", 1,2,3]
print(is_mumber("a", my_list))
print(is_mumber("d", my_list))
print(is_mumber(1 , my_list))
print(is_mumber(4 , my_list))    
    
    









