#!/usr/bin/env python3
from math import factorial

def digit_sum(number: str) -> int:
    """Returns the sum of all of the digits in a given number"""
    runningsum=0
    for i in range(len(number)):
        digit=int(number[i])
        runningsum+=digit
    return runningsum

number=str(factorial(100))
print(digit_sum(number))