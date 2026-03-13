'''import math
def safe_sqrt(x):
    try:
        if x<0:
            raise ValueError("cannot take negative numbers")
        return math.sqrt(x)
    except ValueError as e:
        print(f"Error: {e}")
        return None
    finally:
        print(f"called with {x}")
print(safe_sqrt(-4))
print(safe_sqrt(16))'''

#Write a function safe_divide(a, b) that handles ZeroDivisionError and prints a friendly message instead of crashing.
'''def safe_divide(a,b):
    try:
        return(a/b)
    except TypeError:
        return ("values should be integers ")
    except ZeroDivisionError:
        return ("b cannot be zero")
print(safe_divide(2,0))
print(safe_divide(10,5))'''

#Write a function get_element(lst, index) that handles IndexError when accessing a list element.
'''def get_element(list1,index):
    try:
        for i in range(len(list1)):
            return list1[index]
    except IndexError:
        return("Index out of range")
print(get_element([2,3,4,5,6,7],6))
print(get_element([2,3,4,5,6,7],5))'''

'''Write a safe_divide(a, b) with all four blocks:
try — divide a by b
except — handle zero division
else — print "Division successful" only if no error
finally — always print "Operation complete"'''

'''def safe_divide(a,b):
    try:
        result=a/b
    except ZeroDivisionError:
        return('b cannot be zero')
    else:
        print("Division successful")
    finally:
        print("Operation complete")
    return result
print(safe_divide(4,0))
print(safe_divide(10,5))'''

# Then write a load_number_from_input() function that keeps asking the user for a number until they give a valid one — 
#use a while True loop with try/except.

'''def load_number_from_input():
    while True:
        number= input()
        try:
            number=int(number)
            print(number)
            break
        except ValueError:
            print ("only numeric values are accepted")
load_number_from_input()'''

#Hackerrank write a function

'''def is_leap(year):
    leap = False
    if year% 400==0:
        leap=True 
    elif year%100==0:
        leap=False
    elif year %4==0:
        leap=True
    else: 
        return leap
    return leap

year = int(input())
print(is_leap(year))'''