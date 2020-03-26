#!/usr/bin/python3.7

# string
str1 = "ssss"
# raw string
str2 = r"12\nw  q\t"
# unicode string
str3 = u"\u266A\u266A\u266A\u266A"
# bytes
str4 = b"606162"
# escape character
str5 = "Hello \"world\""

print(type(str1), str1)
print(type(str2), str2)
print(type(str3), str3)
print(type(str4), str4)
print(type(str5), str5)

ll = [0,1,2,3,4]
dd = {'a': 1, 1 : 'a'}

print(type([]))
print(type({}))
print(type([]) is list)
print(isinstance(ll, list))
print(isinstance(dd, list))

# append to immutable creates new object
s1 = "aaa"
s2 = s1
s2 += "bbb"

print("id(s1)", id(s1), s1)
print("id(s2)", id(s2), s2)

# append to mutable change object
l1 = [0,1,2]
l2 = l1
l2 += [3,4,5]
print("id(l1)", id(l1), l1)
print("id(l2)", id(l2), l2)

"""immutable: bool, integer, float, strings, tuple frozenset"""
"""mutable: list dict set"""

x1 = 456
x2 = 457
x3 = x1 + 2
print("id(x1)", id(x1), x1)
print("id(x2)", id(x2), x2)
print("id(x3)", id(x3), x3)
# x3 is immutable
x3 += 0
print("id(x3)", id(x3), x3)

# text formatting
print("today is {}, ".format("monday"))
print("today is {0}, {1:.3f}, val = {x}".format("monday", 12.3, x = "aaa"))
print(f"aaa {x1}")
print("abcdefgh"[0:3])
print("abcdefgh"[0:-2])
print([0,1,2,3,4,5][0:4])
print((0,1,2,3,4,5)[0:3])

print("x" * 80)

# part 1
zen = \
"""1.Beautiful is better than ugly.
2.Explicit is better than implicit.
3.Simple is better than complex. (Has been edited from the Command-line)
4.Complex is better than complicated
5.Flat is better than nested.
6.Sparse is better than dense.
7.Readability counts.
8.Special cases aren't special enough to break the rules.
9.Although practicality beats purity.
10.Errors should never pass silently.
11.Unless explicitly silenced.
12.In the face of ambiguity, refuse the temptation to guess.
13.There should be one-- and preferably only one --obvious way to do it.
14.Although that way may not be obvious at first unless you're Dutch.
15.Now is better than never.
16.Although never is often better than *right* now.
17.If the implementation is hard to explain, it's a bad idea."""

def lookup(text):
    count = 0
    position = zen.find(text)

    while position != -1:
        count += 1
        position = zen.find(text, position + 1)
    
    return count

print("count better", lookup("better"))
print("count never", lookup("never"))
print("count is", lookup("is"))
print("zen upper")
print(zen.upper())
print("zen replace")
print(zen.replace("i", "&"))

print("x" * 80)

# part 2
number = 2135

def get_digits(number):
    digits = []
    
    while number != 0:
        digits.append(number % 10)
        number = number // 10
    return digits

def multiply_digits(digits):
    result = 1

    for digit in digits:
        result *= digit
    
    return result

digits = get_digits(number)

print("digits", digits)
print("multiply digits result", multiply_digits(digits))

digits.reverse()
print("reversed digits", digits)

digits.sort()
print("sorted digits", digits)

print("x" * 80)

# part 3
x = 44
y = 55
print("x =", x, "y =", y)
print("          x               y")
print("         ", id(x), id(y), )
x = x + y; print("x = x + y", id(x), id(y))
y = x - y; print("y = x - y", id(x), id(y))
x = x - y; print("x = x - y", id(x), id(y))
print("x =", x, "y =", y)