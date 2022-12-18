#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        pi = number % 10
    else:
        pi = number % -10
        pi = pi * -1
    print("{:d}".format(pi), end='')
    return pi
