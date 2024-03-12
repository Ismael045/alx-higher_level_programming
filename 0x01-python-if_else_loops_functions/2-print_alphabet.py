#!/usr/bin/python3

# Python program that:
# demonstrates how to print the ASCII alphabet in lowercase
# demonstrates how to use a loop to affect program output
#


for ascii_code in range(97, 123):

    print("{:c}".format(ascii_code), end='')
