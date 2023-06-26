#!/usr/bin/python3
# 0-safe_print_list.py
def safe_print_list(my_list, x):
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
        print("")
        return (count)
