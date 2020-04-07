#!/usr/bin/python3.7

from math import pi, \
                 pow

def rectangle_area(a, b):
    """This function calculates area of recrangle."""

    return a * b

def right_traingle_area(a, b):
    """This function calculates area of right triangle."""

    return a * b / 2
    
def circle_area(r):
    """This function calculates area of circle."""

    return pi * pow(r, 2)