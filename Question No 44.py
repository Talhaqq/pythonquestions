"""Your task in this exercise is as follows:
Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.
Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of
opening/closing brackets (in that order), none of which mis­nest.
"""




def Check_Order_Matrix(String):
    if String.startswith("[") and String.endswith("]"):
        print(True)
    else:
        print(False)
String = "[]][[]][]][][]"
Check_Order_Matrix(String)