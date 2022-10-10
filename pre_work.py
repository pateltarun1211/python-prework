# Question 1
# Write a function to print "hello_USERNAME!"
# USERNAME is the input of the function. The first line of the code has been defined as below.
from doctest import FAIL_FAST


def hello_name():
    """Display inputted username"""
    user_name = input("Enter your username: ")
    print("hello_" + user_name + "!")

hello_name()


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    """Print odd numbers up to a limit."""
    current_number = 0
    while current_number <= 100:
        if current_number % 2 != 0:
            print(current_number)
        current_number += 1

first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    """Return max number in a given list."""
    # First number in list is the largest initially.
    max_num = list[0]
# Go through the list and compare each number to max_num
# if number is larger it will then be the new max_num
    for num in list:
        if num > max_num:
            max_num = num
# Once it goes through the list have it return the max value
    return max_num

list = [5, 2, 51345, 3424, 10934]
print(max_num_in_list(list))

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, 
# but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    # If we want a_year to be divisible by 4 then remained should be 0
    # If we want a_year to not be divisible by 100 we want the remained to not be 0
    # Print True due to it meeting the requirements for a leap year.
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(True)
    # If a_year is divisible by 400 remainder is 0 and it is a leap year
    elif a_year % 400 == 0:
        print(True)
    # If it doesn't meet the set parameters; it is not a leap year.
    else:
        print(False)

is_leap_year(2022)
type(is_leap_year(2022))

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
# The return should be boolean Type.

def is_consecutive(a_list):
    """Return bool for testing if list is consecutive"""
    return a_list == list(range(min(a_list), max(a_list) + 1))

list1 = [2, 4, 5, 1, 6, 3]
print(is_consecutive(list1))

list2 = [1, 2, 3, 4, 5]
print(is_consecutive(list2))