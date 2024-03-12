#!/usr/bin/python3

# Python program that:
# demonstrates how to determine if a number stored in a variable is
# positive or negative
# demonstrates how to use if...elif conditions to determine the program output
#
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number} is positive\n")
elif number == 0:
    print(f"{number} is zero\n")
else:
    print(f"{number} is negative\n")

