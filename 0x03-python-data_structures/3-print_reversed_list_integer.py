#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n=len(my_list)
    if my_list:
        my_list.reverse()
        for j in range(n):
            print("{:d}".format(my_list[j]))
