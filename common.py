#!/usr/bin/python3.7

from sys import exit
from math import sqrt
from area import circle_area, \
                 rectangle_area, \
                 right_traingle_area

from random import randint

def get_integer_from_input(message = "enter integer value: "):
    """This function gets integer value entered by user.
    Exits in case of failure."""

    value = input(message)

    try:
        value = int(value)
    except ValueError:
        exit("input error: value must be integer")
    return value

def get_positive_float_from_input(message = "enter positive float value: "):
    """This function gets positive float value entered by user.
    Exits in case of failure."""

    value = input(message)

    try:
        value = float(value)

        if value < 0:
            exit("input error: value must be positive")

    except ValueError:
        exit("input error: value must be float")

    return value

def count_match(string, what):
    """This function count all matches in string."""

    count = 0
    position = string.find(what)

    while position != -1:
        count += 1
        position = string.find(what, position + 1)
    
    return count

def get_integers_digits(integer):
    """This function store integers digits in list."""

    digits = []
    
    while integer != 0:
        digits.append(integer % 10)
        integer = integer // 10
    
    return digits

def multiply_digits(digits):
    """This function provides multiplication of digits."""

    result = 1

    for digit in digits:
        result *= digit
    
    return result

def factorial_recursion(integer):
    """This function calculates factorial using recursion."""

    if integer > 1:
        return integer * factorial_recursion(integer - 1)
    else:
        return 1

def factorial_loop(integer):
    """This function calculates factorial using for loop."""
    
    result = 1

    for i in range(1, integer + 1):
        result *= i

    return result

def string_words_reverse(string):
    """This function puts strings words in opposite direction."""

    words = string.split()
    words.reverse()

    return words

def integer2string(integer):
    """This function cast integer to string."""

    return str(integer)

def make_wellcome_message(login):
    """This function format message during login procedure."""

    return 'hello {}'.format('my love' if login == 'johnny' else login)

def is_travel_successfull(distance):
    """This function test if travel is successfull."""

    GAS_RATE = 25
    GALONS_COUNT = 2

    return True if GAS_RATE * GALONS_COUNT >= distance else False

def is_available_bus_sits(capacity, on, wait):
    """This function tests if there is enought sits in bus."""

    return 1 if (capacity - on) >= wait else 0

def test_banjo_player_name():
    """This function tests banjo player name and format message."""

    name = input('Are you playing banjo? Enter your name: ')

    if not name:
        exit("error: you doesn't entered name!")

    if name[0] == 'R' or name[0] == 'r':
        msg = ' plays banjo'
    else:
        msg = ' does not play banjo'
    
    return name + msg

def test_input_yes_no(value):
    """This function tests input argument and returns boolean result."""

    return 'Yes' if value else 'No'

def counting_sheep(sheeps):
    """This function counts True in list."""
    
    count = 0

    for sheep in sheeps:
        if sheep: count += 1
    
    return count

def is_correct_tail(body, tail):
    """This function test match 'tail' in 'body' endings."""

    if len(tail) > len(body):
        exit("error: 'tail' size is bigger than 'body'")
    
    sub = body[-len(tail) : ]
    
    return True if sub == tail else False

def get_min_and_max():
    """This function finds minimum and maximum values in input list of 3 elements."""

    COUNT = 3
    values = []

    for i in range(COUNT):
        values.insert(i, get_integer_from_input())

    print('provided values is', values)
    print('min = {}, max {}'.format(min(values), max(values)))

def what_number():
    """This function tests integers properties from 1 t0 10"""

    MIN = 1
    MAX = 10

    print('testing values from {} to {}'.format(MIN, MAX))

    for i in range(MIN, MAX + 1):
        if i % 2 == 0:
            print(i, 'is even')
        elif i % 3 == 0:
            print(i, 'is multiple 3')
        else:
            print(i, 'not multiple 2 or 3')

def make_login_procedure():
    """This function implements login procedure."""
    
    state = False
    count = 3
    LOGIN = 'abc123'

    while count > 0:
        value = input('enter your login ({} tries left): '.format(count))
        count -= 1

        if LOGIN == value:
            state = True
            print('you successfully logged in')

            break
    else:
        print("you failed to login")
    
    return state

def parse_integers():
    """This function takes integers from input that bigger than 0.
    In other case quits."""

    while True:
        value = get_integer_from_input()

        if value > 0:
            print('{}'.format(value))
        else:
            print('provided integer is less than 1, quit')
            break
            
def parse_pack_integers():
    """This function takes N integers from input that bigger than 0.
    In other case quits. N is set during first input and should not exceed 5."""

    count = get_integer_from_input("enter how many integers need to be tested: ")

    MIN = 1
    MAX = 5

    if count >= MIN and count <= MAX:
        i = 0

        while i < count:
            value = get_integer_from_input('enter next integer: ')

            if value > 0:
                print('{}'.format(value))
            else:
                print('provided integer is less than 1, quit')
                break

            i += 1
    else:
        print('error: provided invalid number of input integers')

def is_prime():
    """This function test if integers from 10 to 30 are prime."""
    MIN = 10
    MAX = 30

    print('test if integers in range from {} to {} are prime'.format(MIN, MAX))
    
    for i in range(MIN, MAX + 1):
        prime = True

        for j in range(2, 10):    
            if i % j == 0:
                print('{} not prime, {} * {}'.format(i, j, i // j))
                prime = False
                
                break
        if prime:
            print('{} is prime'.format(i))

def calculate_mean(*numbers):
    """This function calculates mean of arbitrary number of numerical values."""

    return sum(numbers)/len(numbers)

def make_abs(value):
    """This function transforms negative value to positive."""

    return abs(value)

def find_max(*numbers):
    """This function finds maximum value of a and b."""

    return max(numbers)

def area_of_shape():
    """This function calculates area of given shape."""

    shapes = {1 : 'rectangle', 2 : 'right triangle', 3 : 'circle'}

    print('shape types:')

    for key in shapes.keys():
        print(key, shapes[key])

    key = get_integer_from_input('enter shape id: ')

    if key in shapes:
        if key == 1:
            a = get_positive_float_from_input('enter side a length: ')
            b = get_positive_float_from_input('enter side b length: ')

            result = rectangle_area(a, b)
            print('rectangle {:.2f} {:.2f} area is {:.2f}'.format(a, b, result))
        elif key == 2:
            a = get_positive_float_from_input('enter side a length: ')
            b = get_positive_float_from_input('enter side b length: ')

            result = right_traingle_area(a, b)
            print('right triangle {:.2f} {:.2f} area is {:.2f}'.format(a, b, result))
        else:
            r = get_positive_float_from_input('enter circle radius: ')

            result = circle_area(r)
            print('circle {:.2f} area is {:.2f}'.format(r, result))
    else:
        print('error: provided invalid shape id {}'.format(key))

def sum_of_digits():
    """This function calculates sum of integers digits."""

    integer = get_integer_from_input()
    digits = get_integers_digits(integer)

    return sum(digits)

class point:
    """This class intended to store 2D point coordinates."""
    def __init__(self, x, y):
        """This method constructs class object."""
        self.x = x
        self.y = y

    def __sub__(self, point):
        """This method calculates distance between points."""
        dx = (self.x - point.x) ** 2
        dy = (self.y - point.y) ** 2
        
        return sqrt(dx + dy)
    
    def __str__(self):
        """This method print point coordinates."""

        return 'x = {} y = {}'.format(self.x, self.y)

def guess():
    """This function provides guess integer [1, 100] game."""
    value = randint(1, 100)
    version = 0
    print('guess integer in 1 .. 100 range!')

    while version != value:
        version = get_integer_from_input('version: ')

        if value > version:
            print('bigger')
        elif value < version:
            print('lesser')

    else:
        print('congratulations, you guessed value {}!'.format(value))