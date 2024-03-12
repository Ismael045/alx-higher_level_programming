#!/usr/bin/python3

# Python program that:
# demonstrates how to print the ASCII alphabet in lowercase except 'q' and 'e'
# demonstrates how to use a loop, a loop clause and an if condition to
# affect program output
#

for i in range(97, 123):
    if chr(i) not in "qe":
        print(chr(i), end="")
