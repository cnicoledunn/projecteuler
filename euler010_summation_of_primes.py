#!/usr/bin/env python3
import math

def isprime(x:int):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True


s = []

for x in range(2, 2000000):
    if isprime(x):
        s.append(x)

print(sum(s))


