#!/usr/bin/python3.7

from sys import exit
from common import get_integer_from_input

# get integers
a = get_integer_from_input('enter integer a value: ')
b = get_integer_from_input('enter integer b value: ')

print('a + b =', a + b)
print('a - b =', a - b)
print('a * b =', a * b)

# test denominator
if(b == 0):
    exit('error: division by zero')

print('a / b = {:.2f}'.format(a / b))

# get and print information
name  = input('what is your name? ')
age   = get_integer_from_input('how old are you? ')
place = input('where do you live? ')

print('Hello', name)
print('Your age is', age)
print('You live in', place)
