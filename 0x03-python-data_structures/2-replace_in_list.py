#!/usr/bin/python3
# 2-replace_in_list
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return list(my_list)
    new_list = list(my_list)
    new_list[idx] = element
    return new_list
