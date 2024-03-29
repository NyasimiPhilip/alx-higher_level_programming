#!/usr/bin/python3

def safe_print_list(my_list, x):
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print()  # Add a new line after printing the numbers
    return (count)
