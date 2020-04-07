#!/usr/bin/python3.7

from common import get_integer_from_input

def add(a, b):
    """This function provides addition."""

    return a + b

def sub(a, b):
    """This function provides substraction."""

    return a - b

def mul(a, b):
    """This function provides multiplication."""

    return a * b

def div(a, b):
    """This function provides division."""

    return a / b

def print_operations(ops):
    """This function print available operations."""

    for key in ops.keys():
        print('{} is {}'.format(ops[key], key))

def operation():
    """This function provides operation on user input."""

    ops = {-1 : 'exit', 0 : 'help', 1 : '+   ', 2 : '-   ', 3 : '*   ', 4 : '/   '}

    print_operations(ops)

    key = get_integer_from_input('enter operation id: ')

    while key not in ops:
        if key == 0:
            print_operations(ops)
        elif key == 1:
            a = get_integer_from_input('enter a value: ')
            b = get_integer_from_input('enter b value: ')

            print('{} + {} = {}'.format(a,b, add(a, b)))
        elif key == 2:
            a = get_integer_from_input('enter a value: ')
            b = get_integer_from_input('enter b value: ')

            print('{} - {} = {}'.format(a,b, sub(a, b)))
        elif key == 3:
            a = get_integer_from_input('enter a value: ')
            b = get_integer_from_input('enter b value: ')

            print('{} * {} = {}'.format(a,b, mul(a, b)))
        elif key == 4:
            a = get_integer_from_input('enter a value: ')
            b = get_integer_from_input('enter b value: ')

            print('{} / {} = {}'.format(a,b, div(a, b)))
        else:
            print('provided invalid operation id {}'.format(key))
            break

        key = get_integer_from_input('enter operation id: ')
    else:
        print('bye')