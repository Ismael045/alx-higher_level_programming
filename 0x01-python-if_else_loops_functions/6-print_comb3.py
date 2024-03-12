#!/usr/bin/python3
# Python program that:
# demonstrates how to print the smallest, unique combinations of two digits
# demonstrates how to use loops and an if condition to affect program output
#

for i in range(0, 8):
    for j in range(i + 1, 10):
        print(f"{i}{j}, ", end="")
print("89")
