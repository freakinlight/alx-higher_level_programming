#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        m = my_list[0]
        for j in my_list:
            if j > m:
                m = j
        return m
    return None
