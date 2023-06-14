#!/usr/bin/python3
# 3-infinite_add.py
if __name__  == "__main__":
import sys
args = sys.argv[1:]
int_args = [int(arg) for arg in args]
sum_args = sum(int_args)
print(sum_args)
