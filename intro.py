# Print and input
name = input('What is your name? ')
print('Hello, ' + name)

# Terms

# Fundamental Data Types
# int (whole numbers)
print(type(2+4))
# converting to int
int('100')

# float (decimal numbers). float takes up more space than int
print(type(2/4))
print(type(9.9+1.1))

# complex (ie, complex numbers)
# bool
True
False

# str
# Note: String Are Immutable (can't reassign part of a list)
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

# Converting to string
str(100)

# Escape sequences (\, \t adds tab, \n adds line)
weather = 'It\'s sunny'

# Formatted string
print(f'Hi, my name is {first_name} {last_name}.')
print('Hi, my name is {} {}.'.format('Irha', 'Ali'))
print('Hi, my name is {1}, {0}.'.format('Irha', 'Ali'))
print('Hi, my name is {new_first_name} {new_last_name}.'.format(new_first_name = 'Pablo', new_last_name = 'Escobar'))

# Subsdtring [start:stop:stepover]
selfish = '01234567'
print(selfish[0:8])
print(selfish[0:])
print(selfish[:8])
print(selfish[0:8:2])
print(selfish[-1])
# Reverse the string
print(selfish[::-1])

# * in strings
print('*' * 10)

# Data Structures (list, tuple, set): A way to organize data
# list (like array)
# List has a lot of the same methods strings have
list = [1, 2.5, 3, 'a', True]
print(list)
# To copy the list so that you can modify it but not the original
list2 = list[:]
# instead of
list2 = list
# List methods (put . at the end of the list variable)
basket = [1,2,3,4,5,'b']
# Adding
basket.extend([100])
# Removing
basket.pop()
# Get intex
basket.index('b')
'b' in basket # returns True or False
basket.count('b')
basket.sort() # sorts the list (modies original list)
sorted(basket) # sorts the list (creates new list)
basket.reverse() # reverse the list (modies original list)
a,b,c, *other, d = [1,2,3,4,5,6,7,8]
print(other)

# tuple (basically immutable list)
# They're faster than list
my_tuple = (1,2,3,4,5)
print(my_tuple)
print(my_tuple[1])
print(5 in my_tuple)

# set


# dict (like object in Javascript)
# The dictionary key needs to be a data type that is immutable
# Key has to be unique
dictionary = {
    'a': 1,
    'b': 2
}


# Variables (Note: must be in snake_case.
# _ at the beginning indicates private variables)
# Don't use keywords in python as a variable name
# all caps variable indicate the variable is a constant
# How to assign multiple variables values
a,b,c = 1,2,3
print(a, b, c)

# Classes (custom types)

# Specialised Data Types

# None (absense of value)
# When you wanna initialize a variable but not assign it a value
weapons = None

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

# Built-in methods (functions only used by a certain data type)
# Eg. Length of a string
print('Lenght of a string', len('1234567'))

# Best Practices
