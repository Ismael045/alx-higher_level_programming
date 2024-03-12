#!/usr/bin/python3

# Python program that:
# demonstrates how to print the ASCII alphabet in lowercase except 'q' and 'e'
# demonstrates how to use a loop, a loop clause and an if condition to
# affect program output
#

for ascii_code in range(97, 123):
    if ascii_code == 101 or ascii_code == 113:
        continue

    print("{:c}".format(ascii_code), end='')
