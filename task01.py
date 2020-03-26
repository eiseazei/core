#!/usr/bin/python3.7

import sys

def get_integer(msg):
    val = input(msg)
    # test input
    try:
        val = int(val)
    except ValueError:
        sys.exit("error: input must be integer")
    return val

# get integer
a = get_integer("enter integer value: ")
b = get_integer("enter integer value: ")

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)

# test denominator
if(b == 0):
    sys.exit("error: division by zero")

print("a / b =", a / b)

# get and print information
name  = input("what is your name? ")
age   = get_integer("how old are you? ")
place = input("where do you live? ")

print("Hello", name)
print("Your age is", age)
print("You live in", place)
