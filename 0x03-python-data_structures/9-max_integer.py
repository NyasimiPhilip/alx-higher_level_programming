#!/usr/bin/python3
# 9-max_integer.py
#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    maxNum = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > maxNum:
            maxNum = my_list[i]
            return (maxNum)
