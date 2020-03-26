#!/usr/bin/python3.7

from task01 import get_integer

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
    a = get_integer()
    b = get_integer()

    if(a == b):
        pass
    elif(a < b):
        print(b, " is bigger ")
    else:
        print(a, " is bigger ")

    #---------------------------------------------------------------------------
    # test odd
    a = get_integer()

    if a % 2:
        print(a, "odd")
    else:
        print(a, "even")