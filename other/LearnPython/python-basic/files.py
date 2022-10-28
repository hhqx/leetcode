"""
this is a docstring

"""

print(__doc__)

"""
We can use the type() function to know which class a variable or a value belongs to 
and isinstance() function to check if it belongs to a particular class.
"""

## decimal module
import decimal

print(0.1)

print(decimal.Decimal(0.1))

# fractions module
import fractions

print(fractions.Fraction(1.5))

print(fractions.Fraction(5))

print(fractions.Fraction(1, 3))

import fractions

# As float
# Output: 2476979795053773/2251799813685248
print(fractions.Fraction(1.1))

# As string
# Output: 11/10
print(fractions.Fraction('1.1'))

from fractions import Fraction as F

print(F(1, 3) + F(1, 3))

print(1 / F(5, 6))

print(F(-3, 10) > 0)

print(F(-3, 10) < 0)

# math and random modules
import math

print(math.pi)

print(math.cos(math.pi))

print(math.exp(10))

print(math.log10(1000))

print(math.sinh(1))

print(math.factorial(6))

import random

print(random.randrange(10, 20))

x = ['a', 'b', 'c', 'd', 'e']

# Get random choice
print(random.choice(x))

# Shuffle x
random.shuffle(x)

# Print the shuffled x
print(x)

# Print random element
print(random.random())

## list
# Appending and Extending lists in Python
odd = [1, 3, 5]

odd.append(7)

print(odd)

# append multiple items
odd.extend([9, 11, 13])

print(odd)
# Demonstration of list insert() method
odd = [1, 9]
odd.insert(1, 3)

print(odd)

# insert multiple items
odd[2:2] = [5, 7]

print(odd)

# delete items of list
# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
del my_list[2]

print(my_list)

# delete multiple items
# we can also delete items in a list by assigning an empty list to a slice of elements.
del my_list[1:5]  # or my_list[1:5] = []

print(my_list)

# delete the entire list
del my_list

# Error: List not defined
# print(my_list)

# clear the whole list
a = [1, 2, 3]
a[:] = []  # or a.clear()

# Example on Python list methods

my_list = [3, 8, 1, 6, 8, 8, 4]

# Add 'a' to the end
my_list.append('a')

# Output: [3, 8, 1, 6, 8, 8, 4, 'a']
print(my_list)

# remove the first item that has a value of 1
my_list.remove(1)

# Index of first occurrence of 8
print(my_list.index(8))   # Output: 1

# Count of 8 in the list
print(my_list.count(8))  # Output: 3


# Python program to shuffle a deck of card
# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("You got:")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])

# list comprehension
matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print(transpose)


# format_map
# format_map(mapping) is more flexible than format(**mapping) as you can have missing keys.
class Coordinate(dict):
    def __missing__(self, key):
        return key

print('({x}, {y})'.format_map(Coordinate(x='6')))
print('({x}, {y})'.format_map(Coordinate(y='5')))
print('({x}, {y})'.format_map(Coordinate(x='6', y='5')))
