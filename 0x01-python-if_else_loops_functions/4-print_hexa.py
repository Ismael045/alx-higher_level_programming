#!/usr/bin/python3

# Python program that:
# demonstrates how to print all numbers from 0 to 98 in decimal and in
# hexadecimal
# demonstrates how to use a loop to affect program output
#

for i in range(0,99):
    print(f"{i} = 0x{i:x}" ,end="\n")
