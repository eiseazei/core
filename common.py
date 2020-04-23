#!/usr/bin/python3.7

from sys import exit
from math import sqrt
from random import randint

def get_integer_from_input(message = "enter integer value: ") -> int:
    """This function gets integer value entered by user.
    Exits in case of failure."""

    value = input(message)

    try:
        value = int(value)
    except ValueError:
        exit("input error: value must be integer")
    return value

def get_positive_float_from_input(message = "enter positive float value: ") -> int:
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

def count_match(string, what) -> int:
    """This function count all matches in string."""

    count = 0
    position = string.find(what)

    while position != -1:
        count += 1
        position = string.find(what, position + 1)
    
    return count

def get_integers_digits(integer) -> list:
    """This function store integers digits in list."""

    digits = []
    
    while integer != 0:
        digits.append(integer % 10)
        integer = integer // 10
    
    return digits

def multiply_digits(digits) -> int:
    """This function provides digits multiplication."""

    result = 1

    for digit in digits:
        result *= digit
    
    return result

def factorial_recursion(integer) -> int:
    """This function calculates factorial using recursion."""

    if integer > 1:
        return integer * factorial_recursion(integer - 1)
    else:
        return 1

def factorial_loop(integer) -> int:
    """This function calculates factorial using for loop."""
    
    result = 1

    for i in range(1, integer + 1):
        result *= i

    return result

def string_words_reverse(string) -> str:
    """This function puts strings words in opposite direction."""

    words = string.split()
    words.reverse()

    return words

def integer2string(integer) -> str:
    """This function cast integer to string."""

    return str(integer)

def make_wellcome_message(login) -> str:
    """This function format message during login procedure."""

    return 'hello {}'.format('my love' if login == 'johnny' else login)

def is_travel_successfull(distance) -> bool:
    """This function test if travel is successfull."""

    GAS_RATE = 25
    GALONS_COUNT = 2

    return True if GAS_RATE * GALONS_COUNT >= distance else False

def is_available_bus_sits(capacity, on, wait) -> int:
    """This function tests if there is enought sits in bus."""

    return 1 if (capacity - on) >= wait else 0

def test_banjo_player_name() -> str:
    """This function tests banjo player name and format message."""

    name = input('Are you playing banjo? Enter your name: ')

    if not name:
        exit("error: you doesn't entered name!")

    if name[0] == 'R' or name[0] == 'r':
        msg = ' plays banjo'
    else:
        msg = ' does not play banjo'
    
    return name + msg

def test_input_yes_no(value) -> str:
    """This function tests input argument and returns boolean result as string."""

    return 'Yes' if value else 'No'

def counting_sheep(sheeps) -> int:
    """This function counts True in list."""
    
    count = 0

    for sheep in sheeps:
        if sheep: count += 1
    
    return count

def is_correct_tail(body, tail) -> bool:
    """This function test match 'tail' in 'body' endings."""

    if len(tail) > len(body):
        exit("error: 'tail' size is bigger than 'body'")
    
    sub = body[-len(tail) : ]
    
    return True if sub == tail else False

def get_min_and_max() -> None:
    """This function finds minimum and maximum values in input list of 3 elements."""

    COUNT = 3
    values = []

    for i in range(COUNT):
        values.insert(i, get_integer_from_input())

    print('provided values is', values)
    print('min = {}, max {}'.format(min(values), max(values)))

def what_number() -> None:
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

def make_login_procedure() -> bool:
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

def parse_integers() -> None:
    """This function takes integers from input that bigger than 0.
    In other case quits."""

    while True:
        value = get_integer_from_input()

        if value > 0:
            print('{}'.format(value))
        else:
            print('provided integer is less than 1, quit')
            break

def parse_pack_integers() -> None:
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

def is_prime() -> None:
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

# 6

def calculate_mean(*numbers) -> int:
    """This function calculates mean of arbitrary number of numerical values."""

    return sum(numbers)/len(numbers)

def make_abs(value) -> int:
    """This function transforms negative value to positive."""

    return abs(value)

def find_max(*numbers) -> int:
    """This function finds maximum value of a and b."""

    return max(numbers)

def sum_of_digits() -> int:
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

def sticks() -> None:
    """This function implement sticks game."""
    
    print('sticks game began')
    left = 21

    bob = 1
    left -= bob
    print('Bob takes {} -> {} sticks left'.format(bob, left))

    while left > 3:
        jim = randint(1, 3)
        left -= jim
        print('Jim takes {} -> {} sticks left'.format(jim, left))

        bob = 4 - jim
        left -= bob
        print('Bob takes {} -> {} sticks left'.format(bob, left))

def filter_words(message) -> None:
    """This function capitalize string."""

    print(message)
    message = message.capitalize()
    print(message)

def create_array(n) -> list:
    """This function creates an array, populated with integers from 1 to n."""

    res=[]
    i = 1
    while i <= n:
        res += [i]
        i += 1

    return res

# 7
def guess() -> None:
    """This function provides guess integer [1, 100] game."""

    MIN = 1
    MAX = 100
    value = randint(MIN, MAX)
    version = 0

    print('guess integer in {} .. {} range!'.format(MIN, MAX))

    while version != value:
        version = get_integer_from_input('version: ')

        if value > version:
            print('bigger')
        elif value < version:
            print('lesser')

    else:
        print('congratulations, you guessed value {}!'.format(value))

def count_pos_sum_neg(array) -> []:
    """This function counts positive and sum of negative vaues in array"""
    cp = 0
    ns = 0

    for i in array:
        if i >= 0:
            cp += 1
        else:
            ns += i
    
    return cp, ns

def reverse_order(array) -> list:
    """This function reverse array"""

    return array[::-1]

def sum_of_multiple_3_5() -> int:
    """This function make sum of multiple 3 and 5 numbers"""

    sum = 0

    for i in range(10):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    
    return sum

# 8
def summation(num) -> int:
    """This function makes numbers summation"""

    return sum(range(1, num + 1))

def list_animals(animals) -> str:
    """This function formats animals string"""
    
    string = ''

    for i in range(len(animals)):
        string += str(i + 1) + '. ' + animals[i] + '\n'

    return string

def double_chars(message) -> str:
    """This function doubles every character in message"""

    return ''.join([c * 2 for c in message])

# 9
def is_upper_case(message) -> bool:
    """This function tests if string in uppercase"""
    
    return message.upper() == message

def sort_textbooks(textbooks) -> list:
    """This function sorts strings in list ignoring case"""
    
    return sorted(textbooks, key=str.lower)

def shortenToDate(message) -> str:
    """This function shortens date/time string removing time part"""

    date = message.split(sep = ',')

    return date[0]

# 10
class Ball:
    """This class implements dummy ball"""

    def __init__(self, type = 'regular'):
        """This method initialize class properties"""
        self.type = type

    def __str__(self):
        return 'ball type for Ball class is {:s}'.format(self.type)

class Ghost:
    """This class implements dummy ghost"""

    def __init__(self):
        """This method initialize class properties"""
        self.colors = ['white' , 'yellow' , 'purple' , 'red']
        
        i = randint(0, len(self.colors) - 1)

        self.color = self.colors[i]

    def __str__(self):
        return 'color value for Ghost class is {:s}'.format(self.color)

class Human:
    """This class represents information about human"""

    def __init__(self, name):
        """This method initialize class properties"""
        
        self.name = name
        self.sex = 'human'

class Man(Human):
    """This class represents information about man"""

    def __init__(self, name):
        """This method initialize class properties"""
        
        super().__init__(name)
        self.sex = 'man'

class Woman(Human):
    """This class represents information about woman"""

    def __init__(self, name):
        """This method initialize class properties"""
        
        super().__init__(name)
        self.sex = 'woman'

def make_humans():
    """This function make humanoids"""

    m = Man('Adam')
    w = Woman('Eve')

    return [m, w]

class Person:
    """This class implements dummy person"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getPersonInfo(self):
        """This method format information about person"""
        return '{:s} age is {:d}'.format(self.name, self.age)

# 11

def test_integer_odd_even(value) -> None:
    """Test if value is odd or even."""

    if value % 2:
        print('provided value {} is odd'.format(value))
    else:
        print('provided value {} is even'.format(value))

def test_input_integer(message = 'enter arbitrary integer: ') -> int:
    """Test if input is integer and make exception if not."""

    value = input(message)

    try:
        value = int(value)
    except ValueError:
        print('provided value is invalid: "{}" not integer'.format(value))
    
    return value

class ValueExcept(Exception):
    """Exceptions for negative integers."""
    pass

def handle_age_input() -> None:
    """Test provided value for age and make exception if invalid."""

    try:
        value = test_input_integer('enter your age: ')

        if value >= 0:
            test_integer_odd_even(value)
        else:
            raise ValueExcept
    except ValueExcept:
        print('provided age value is negative!')

def num_denum() -> None:
    """Test numinator and denuminator."""

    n = 0
    d = 0

    try:
        string = input('type numinator and denuminator separated by ",": ')

        values = string.split(sep = ',', maxsplit = 1)

        n = int(values[0])
        d = int(values[1])

        result = n / d

    except IndexError:
        pass
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    finally:
        print('{:d} / {:d} = {:2f}'.format(n, d, result))
    
def week_day() -> None:
    """Print week day on input."""

    days = {1 : 'monday', 
            2 : 'tuesday',
            3 : 'wednesday',
            4 : 'thursday',
            5 : 'friday',
            6 : 'saturday',
            7 : 'sunday'}

    name = ''
    
    day = test_input_integer('enter week day number: ')

    try:
        name = days[day]
    except KeyError:
        exit('provided day value {} is invalid'.format(day))
        
    finally:
        print('week day is {}'.format(name))

# 12
def hash_names() -> None:
    """Make hash of names."""

    names = ['bob', 'john', 'bill']
    names = list(map(hash, names))

    print(names)

def filter_red() -> None:
    """Find match 'red' in array"""

    values = ['red', 'green', 'black', 'red', 'brown', 'red', 'blue', 'red', 'red', 'yellow']
    values = list(filter(lambda value: value == 'red', values))

    print(values)

def convers_string2int() -> None:
    """Use map to convert array with str to int."""

    values = ['0', '1', '2']

    array = list(map(int, values))

    print(array)

def convert_miles2km() -> None:
    """Use map to convert miles in km."""

    miles = [12, 13, 14]

    def mil2km(mile):
        return mile * 1.6

    km1 = list(map(mil2km, miles))
    km2 = list(map(lambda value: value * 1.6, miles))

    print(km1)
    print(km2)