# Print and input
name = input('What is your name? ')
print('Hello, ' + name)

# Terms

# Fundamental Data Types
# int (whole numbers)
print(type(2+4))

# float (decimal numbers). float takes up more space than int
print(type(2/4))
print(type(9.9+1.1))

# complex (ie, complex numbers)
# bool
# str
'Hi'
"Hello"
# Multiline string
long_string = '''
WOWZA
O O
---
'''
# Concatenated string
first_name = 'Irha'
last_name = 'Ali'
full_name = first_name + ' ' + last_name
print(full_name)

# list
# tuple
# set
# dict (variables) (Note: must be in snake_case.
# _ at the beginning indicates private variables)
# Don't use keywords in python as a variable name
# all caps variable indicate the variable is a constant
# How to assign multiple variables values
a,b,c = 1,2,3
print(a, b, c)

# Classes (custom types)

# Specialised Data Types

# None (absense of value)

# Actions 
# (operations: +, - , *, /, **, // (round down when dividing),
# %, round, abs, etc)
# Operator precedence (ie. BEDMAS)
print(20 - 3 * 4)

# Binary representation of a number and number representation of a binary
print(bin(5))
print(int('0b101', 2))

# Augmented assignment operator
some_value = 5
some_value += 2 # instead of some_value = some_value + 2
print(some_value)

# Best Practices
