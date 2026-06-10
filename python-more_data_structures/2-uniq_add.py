#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    unique = []

    for num in my_list:
        if num not in unique:
            unique.append(num)
            result += num

    return result
