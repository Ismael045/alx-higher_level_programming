#!/usr/bin/python3

# Python program that:
# demonstrates how to determine if a number stored in a variable is
# positive or negative
# demonstrates how to use if...elif conditions to determine the program output
#

import random
number = random.randint(-10, 10)

if number > 0:
     print("{} is positive".format(number))

elif number > 0:
    print("{} is negative".format(number))

else:
    print("{} is zero".format(number))

