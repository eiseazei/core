#!/usr/bin/python3.7

for i in range(10):
    i += 1
else:
    print("last", i)

i = 0

while i < 10:
    i += 3
else:
    print("last", i)

for i  in "abcdefgh":
    pass

#
val = -1

if val < 0:
    print("negative")
elif val == 0:
    print("zero")
else:
    print("positive")
