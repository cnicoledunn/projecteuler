#!/usr/bin/env python3
from typing import List

def get_fibonacci(max_val: int) -> List[int]:
    """returns a fibonacci sequence"""
    s=[1,2]
    while s[-1]<=max_val:
        s.append(s[-1]+s[-2])
    s.pop()
    return s

def get_evens(numbers: List[int]) -> List[int]:
    """checks whether numbers are even"""
    ret=[]
    for i in numbers:
        if i%2==0:
            ret.append(i)
    return ret

s=get_fibonacci(max_val=4_000_000)
s=get_evens(s)
#s=[x for x in s if x%2==0] -- does same thing as function on line 12
print(sum(s))






