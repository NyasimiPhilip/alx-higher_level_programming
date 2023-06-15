#!/usr/bin/python3
# 12-roman_to_int.py
ROMAN_VALUES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return (None)
    number = 0
    for i in range(len(roman_string)):
        if i + 1 < len(roman_string):
            if ROMAN_VALUES[roman_string[i]] >= ROMAN_VALUES[roman_string[i + 1]]:
                number += ROMAN_VALUES[roman_string[i]]
            else:
                number -= ROMAN_VALUES[roman_string[i]]
            else:
                number += ROMAN_VALUES[roman_string[i]]
                return (number)
