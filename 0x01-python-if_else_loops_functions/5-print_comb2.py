#!/usr/bin/python3

# Python program that:
# demonstrates how to print numbers from 0 to 99
# demonstrates how to use a loop and string formatting to affect program output
#

for number in range(0, 99):

    print("{:02d}, ".format(number), end=", ")

print("99")

