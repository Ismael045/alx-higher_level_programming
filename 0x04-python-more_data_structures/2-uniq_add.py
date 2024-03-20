#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = set()
    for num in my_list:
        total.add(num)
    add = sum(total)
    return add
