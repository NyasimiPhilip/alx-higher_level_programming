#!/usr/bin/python3
# 100-weight_average.py
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    total_weight = 0
    weighted_sum = 0
    for value, weight in my_list:
        weighted_sum += value * weight
        total_weight += weight
    if total_weight == 0:
        return (0)
    return (weighted_sum / total_weight)
