#!/usr/bin/env python3

def get_series(numbers: range) -> str:
    """Takes a given range of integers and returns a sequence of said integers raised to the power of themselves"""
    runningsum=0
    for i in numbers:
        runningsum+=i**i
    return str(runningsum)

numbers = range(1, 1001)
print(get_series(numbers)[-10:])