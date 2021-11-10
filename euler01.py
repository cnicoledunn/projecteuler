#!/usr/bin/env python3

def is_multiple(x: int) -> bool:
    return x%3==0 or x%5==0

s = 0
for x in range(3, 1000):
    if is_multiple(x):
        s=s+x

print(s)