#!/usr/bin/env python3
import math
from typing import Final, List

factors: Final[List[int]] = list(range(11,21))

def divisible_by_all(x: int) -> bool:
    """determines whether x is divisible by all factors in the list named factors"""
    for f in factors:
        if x%f!=0:
            return False
    return True

for x in range(1, math.factorial(20)+1):
    if divisible_by_all(x):
        print(x)
        break




