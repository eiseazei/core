#!/usr/bin/python3.7

from common import get_integer_from_input

def calc_add():
    """This function provides addition."""

    a = get_integer_from_input('enter a value: ')
    b = get_integer_from_input('enter b value: ')

    print('{} + {} = {}'.format(a, b, a + b))

def calc_sub():
    """This function provides substraction."""
    
    a = get_integer_from_input('enter a value: ')
    b = get_integer_from_input('enter b value: ')

    print('{} - {} = {}'.format(a, b, a - b))

def calc_mul():
    """This function provides multiplication."""

    a = get_integer_from_input('enter a value: ')
    b = get_integer_from_input('enter b value: ')

    print('{} * {} = {}'.format(a, b, a * b))

def calc_div():
    """This function provides division."""

    a = get_integer_from_input('enter a value: ')
    b = get_integer_from_input('enter b value: ')

    print('{} / {} = {}'.format(a, b, a / b))

def print_operations(ops):
    """This function print available operations."""

    for key in ops.keys():
        print('{} is {}'.format(ops[key], key))

def operation():
    """This function provides operation on user input."""

    ops = {-1 : 'exit', 0 : 'help', 1 : '+   ', 2 : '-   ', 3 : '*   ', 4 : '/   '}

    print_operations(ops)

    key = get_integer_from_input('enter operation id: ')

    while key in ops:
        if key == -1:
            break
        elif key == 0:
            print_operations(ops)
        elif key == 1:
            calc_add()
        elif key == 2:
            calc_sub()
        elif key == 3:
            calc_mul()
        elif key == 4:
            calc_div()
        else:
            print('provided invalid operation id {}'.format(key))
            break
        key = get_integer_from_input('enter operation id: ')
        
    print('bye')