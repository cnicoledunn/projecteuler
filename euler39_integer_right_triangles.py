#!/usr/bin/env python3
from typing import Dict
from collections import defaultdict

def get_triangles(maxval: int) -> Dict[int, int]:
    """Returns a dictionary containing perimeters as the key and their frequencies as the value"""
    s=defaultdict(int)
    for c in range(0, maxval+1):
        for b in range (0, c):
            for a in range (0, b):
                if a+b+c<=1000:
                    if c**2 == a**2 + b**2:
                        p=a+b+c
                        s[p]+=1
    return s


def counter(scores: Dict[int, int]) -> int:
    """Returns the key associated with the highest value"""
    temp=None
    for p,count in scores.items():
        if temp is None or count>temp[1]:
            temp=(p, count)
    return temp[0]

maxval=1000
print(counter(get_triangles(maxval)))





