#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    largest_value = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if value == largest_value:
            return key
