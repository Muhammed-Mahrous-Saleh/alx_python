#!/usr/bin/python3

def common_elements(set1, set2):
    common = []
    for e in set1:
        if e in set2:
            common.append(e)
    return common
