# So, this will be main fail where I will take notes while
# doing Python 3 Deep Dive course.
# Also, in order to get some experience with Git/GitHub
# I will constantly commit and push the changes to GitHub repo.

# Implicit and Explicit line breaks

some_list = [10,
             20,
             30]

def some_function(a,
                  b,
                  c):
    return a, b, c


a = 11
b = 20
if a > 10\
    and b == 20:
    print('a > 10 and b = 20')


# identifier names
# variable names are case-sensative

my_VAR = 10
my_var = 20

# identifiers cannot be reserved words

'''
None
True
False
and 
or
'''

# when variable name starts with _ , this variable is private
# private variables will not be imported
# however, you still can access it

_my_var = 20

# __ is used for name mangleing

__my_var = 30

# some variable starts with __ and ends with __
# you should not invent your __var__
# there are many duner variables in Python

#__init__():

# package names should be all lover case letters: utilities
# for modules you can you _ : db_utils
# classes uses upper camel case: BankAccount
# function lover-cases, snake case: open_account
# variable snake case: account_id
# constants all-uppercase: MIN_APR

# for more info on code style see PEP8

# Ternary operator
# format: [on_true] if [expression] else [on_false]

a = 30
b = 20
min = a if a < b else b
print(min)

# Functions
# built in functions, len(s)
# some functions need to be imported: from math import sqrt
# we can define our own functions
# to call the function you need to call it with parentheses func_name()
# you can add annotation to function parameters


def my_func(a: int, b: int):
    return a * b

# lambda
# lambda is a function without name
# lambda x: x**2


fn1 = lambda x: x**2
print(fn1(2))


# while loop

# min_length = 2
# while True:
#     name = input('Please, input your name:')
#     if len(name) >= min_length and name.isprintable() and name.isalpha():
#         break
# print('Hello, ', name)

# break - stops current iteration of the loop
# continue - starts the loop from the beginning, skipping all other code after the continue
# didn't know that while loop has else condition.
# the code in else is executed only when while loop ends normally

# try ... except ... finally
#
# finally always runs, no matter if there is an exception or not

a = 10
b = -2

try:
    print(a/b)
except ZeroDivisionError:
    print("you can't devide to Zero")
finally:
    print("this line will always be printed")

