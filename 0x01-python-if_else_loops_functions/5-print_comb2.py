#!/usr/bin/python3

# Python program that:
# demonstrates how to print numbers from 0 to 99
# demonstrates how to use a loop and string formatting to affect program output
#

for i in range(0, 99):
    print(f"{i:02d}" if i > 98 else f"{i:02d}", end=", ")
print(f"99")

