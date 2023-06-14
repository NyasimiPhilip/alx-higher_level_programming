#!/usr/bin/python3
# 3-infinite_add.py
from sys import argv
if __name__ == "__main__":
    total = 0
    fh = len(argv) - 1
    for j in range(1, fh + 1):
        total += int(argv[j])
    print(total)
