# You are given a string and your task is to swap cases. 
# In other words, convert all lowercase letters to uppercase letters and vice versa.


def swap_case(s):
#     return s.swapcase() 

  
def swap_case_loop(s: str):
    swapped_s = ""
    for char in s:
        if char.isupper(): # -> false
            swapped_s = swapped_s + char.lower()
        else: # -> lowercase
            swapped_s = swapped_s + char.upper()
            
    return swapped_s


if __name__ == '__main__':
    s = input("Enter a string: ")
    result = swap_case(s)
    print(result)
 