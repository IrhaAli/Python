# Print and input
name = input('What is your name? ')
print('Hello, ' + name)

############################### Terms ##############################
# Conditional Logic
is_old = True
is_licenced = True

if is_old and is_licenced:
    print('You\'re old enough to drive')
elif is_old:
    print('You\'re old but can\'t drive')
else:
    print('No driving for you')

# Truthy and Falsy
# The falsy values are empty string, 0, null, undefined, None etc

# Ternary Operators
# condition_if_true if condition else condition_if_false

# Short Circuiting (when or is used in an if statement check the easier condition)
is_Friend = True
is_User = True

if is_Friend and is_User:
    print('BFF')

# Logical Operators (and, or, >, <, ==, !=)

# is VS
print(True == 1)  # Truthy Falsey Result: True
print('' == 1)  # Truthy Falsey Result: False
print([] == 1)  # Truthy Falsey Result: False
print(10 == 10.0)  # Result: True
print([1, 2, 3] == [1, 2, 3])  # Result: True

print(True is True)  # Truthy Falsey Result: True
print(1 is 1)  # Result: True
print([] is [])  # Result: False

# For loops (do it for list, dictionary, strings, tuples, sets, anything iterable)
for item in 'Zero to Mastery':
    print(item)

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for key, value in user.items():
    print(key, value)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

# Range
for number in range(0, 10, 2): # 0 to 10 skip by 2
    print(number)

# Enumerate
for i, char in enumerate('Hello'):
    print(i, char) # index i of character as index i

for i, char in enumerate(list(range(100))):
    print(i, char) # index i of character as index i

# While loop (break (break the loop), continue (ignore everything else in the loop for that iteration), pass (good placeholder when you haven't implemented the loop))
condition = True

while condition:
    print(i)
    condition = False
else:
    # The else block only executed if only there's no break in the loop
    print('No breaks in the loop')

# Arguments vs. Parameters

############################## Fundamental Data Types ##############################
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
print('Hi, my name is {new_first_name} {new_last_name}.'.format(
    new_first_name='Pablo', new_last_name='Escobar'))

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
basket = [1, 2, 3, 4, 5, 'b']
# Adding
basket.extend([100])
# Removing
basket.pop()
# Get intex
basket.index('b')
'b' in basket  # returns True or False
basket.count('b')
basket.sort()  # sorts the list (modies original list)
sorted(basket)  # sorts the list (creates new list)
basket.reverse()  # reverse the list (modies original list)
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8]
print(other)

# tuple (basically immutable list)
# They're faster than list
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(my_tuple[1])
print(5 in my_tuple)

# set (unordered collection of unique objects)
# It does not support indexing
my_set = {1, 2, 3, 4, 5, 5}
print(my_set)  # {1, 2, 3, 4, 5}
my_list = [1, 2, 3, 4, 5, 5]
print(set(my_list))
# .difference: difference between two sets
# .discard: removes elements from the set
# .difference_update: the intersection of two sets is removed
# intersection: gives the intersection of two sets
# isdisjoint: true if the two sets are disjoint else false
# issubset: checks if the one set is subset of the other
# issuperset: checks if the one set is superset of the other

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
a, b, c = 1, 2, 3
print(a, b, c)

# Classes (custom types)

# Specialised Data Types

# None (absense of value)
# When you wanna initialize a variable but not assign it a value
weapons = None

############################### Actions ##############################
# (operations: +, - , *, /, **, // (round down when dividing),
# %, round, abs, etc)
# Operator precedence (ie. BEDMAS)
print(20 - 3 * 4)

# Binary representation of a number and number representation of a binary
print(bin(5))
print(int('0b101', 2))

# Augmented assignment operator
some_value = 5
some_value += 2  # instead of some_value = some_value + 2
print(some_value)

# Built-in methods (functions only used by a certain data type)
# Eg. Length of a string
print('Lenght of a string', len('1234567'))

############################### Best Practices ##############################
# GUI (Graphical User Interface)
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

fill = '*'
empty = ' '
# Iterate over the images
for image in picture:
    #  Iterate over the image
    for pixel in image:
        # If a 0 then print empty space, If 1 then print *
        print(fill if (pixel == 1) else empty, end='')
    print('')

# Check for duplicates
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
values = {}
for value in some_list:
    if values[value]:
        duplicates.append(value)
    else:
      values[value] = value

print(duplicates)

# Functions
def say_hello(name):
    print('Hello', name)

say_hello('Irha Ali')