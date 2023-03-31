#!/usr/bin/python3
"""find peak in a list of integers"""

def find_peak(listi):
    length = len(listi)
    if length == 0:
        return None
    maxim = listi[0]
    count = 0
    for i, elem in enumerate(listi):
        temp = maxim
        if elem > temp:
            maxim = elem
        if i < length - 1:
            if elem == listi[i + 1]:
                count = count + 1
    if count == length - 1:
        return listi[i]
    return maxim
