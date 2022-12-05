#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if (number > 5):
  print(f"last digit of {number} is {last_digit} and is greater than 5")
elif (number == 0):
  print(f" last digit of {number} is {last_digit} and is 0")
else :
  print(f" last digit of {number} is {last_digit} and is not less than 6 not 0")
