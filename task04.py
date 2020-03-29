#!/usr/bin/python3.7

from task01 import get_integer

def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

if __name__ == "__main__":
    # for loop
    for i in range(10):
        print(i, end=' ')
        i += 1
    else:
        print("last", i)

    # while loop
    i = 0

    while i < 10:
        print(i, end=' ')
        i += 3
    else:
        print("last", i)

    # empty for loop
    for i  in "abcdefgh":
        pass
    
    # branch
    val = -1

    if val < 0:
        print("negative")
    elif val == 0:
        print("zero")
    else:
        print("positive")

    ll = list(range(10))

    for i in ll:
        if(i % 2 == 0):
            print(i, end=' ')

    print()

    dd = {0 : 'a', 1 : 'b', 2 : 'c', 3 : 'd'}

    for key in dd:
        if(key == 3):
            continue

        dd[key] += " @_@"

    print(dd)

    #---------------------------------------------------------------------------
    # test bigger
    a = get_integer("enter integer 'a' for biggest test ")
    b = get_integer("enter integer 'b' for biggest test ")

    if(a == b):
        pass
    elif(a < b):
        print(b, " is bigger ")
    else:
        print(a, " is bigger ")

    #---------------------------------------------------------------------------
    # test odd
    a = get_integer("enter integer for parity check ")

    if a % 2:
        print(a, "even")
    else:
        print(a, "odd")
    
    #---------------------------------------------------------------------------
    n = 5
    print(n, "! = ", factorial(n), sep='')
    
    
