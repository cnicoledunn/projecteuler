#!/usr/bin/env python3
import math

def isprime(x: int) -> bool:
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

for x in range(int(math.sqrt(600851475143))+1, 1, -1):
    if isprime(x) and 600851475143%x==0:
        print(x)
        break
