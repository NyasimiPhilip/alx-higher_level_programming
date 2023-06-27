#!/usr/bin/python3
def magic_calculation(a, b):
    count = 0
    for f in range(1, 3):
        try:
            if f > a:
                raise Exception('Too Far')
            else:
                count += (a ** b) / f
        except Exception:
            count = b + a
            break
        return count
