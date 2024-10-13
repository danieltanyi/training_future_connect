"""
Problem Statement:
How to swap all uppercase characters to lowercase and vice versa?

Questions:
- How the user will enter the character?
- How it will swap?
- Which commands will be used to convert each other
"""

def swap_case(swap):
    string =""

    for char in swap:
        if char.islower():
            string += char.upper()
        else:
            string += char.lower

            return string
        
        if my_name =="_main_":
            swap =input("Enter string:")
            result=swap_case(swap)
            print("swapped string:" + result)
