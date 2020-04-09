#!/usr/bin/python3.7

from common import get_integer_from_input, \
                   get_positive_float_from_input

from math import pi, \
                 pow

def rectangle_area():
    """This function calculates area of recrangle."""

    a = get_positive_float_from_input('enter side a length: ')
    b = get_positive_float_from_input('enter side b length: ')

    print('rectangle {:.2f} {:.2f} area is {:.2f}'.format(a, b, a * b))

def right_traingle_area():
    """This function calculates area of right triangle."""

    a = get_positive_float_from_input('enter side a length: ')
    b = get_positive_float_from_input('enter side b length: ')

    print('right triangle {:.2f} {:.2f} area is {:.2f}'.format(a, b, a * b / 2))
    
def circle_area():
    """This function calculates area of circle."""

    r = get_positive_float_from_input('enter circle radius: ')

    print('circle {:.2f} area is {:.2f}'.format(r, pi * pow(r, 2)))

def area_of_shape():
    """This function calculates area of given shape."""

    shapes = {1 : 'rectangle', 2 : 'right triangle', 3 : 'circle'}

    print('shape types:')

    for key in shapes.keys():
        print(key, shapes[key])

    key = get_integer_from_input('enter shape id: ')

    if key in shapes:
        if key == 1:
            rectangle_area()
        elif key == 2:
            right_traingle_area()
        else:
            circle_area()
    else:
        print('error: provided invalid shape id {}'.format(key))