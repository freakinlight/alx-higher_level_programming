#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newone = []
    for j in range(len(my_list)):
        if my_list[j] % 2 == 0:
            newone.append(True)
        else:
            newone.append(False)
    return newone
