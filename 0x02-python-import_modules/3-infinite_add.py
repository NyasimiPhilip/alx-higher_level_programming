#!/usr/bin/python3
# 3-infinite_add.py
if __name__ == "__main__":
    import sys
    result = 0
    for i, args in enumerate(sys.argv):
        if i == 0:
            continue
        sum += int(args)
    print(f"{sum:d}")
