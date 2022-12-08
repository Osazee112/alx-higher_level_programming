#!/usr/bin/python3
for j in range(26):
    if j != 4 and j != 16:
        print("{:s}".format(chr(j + ord("a"))), end="")
