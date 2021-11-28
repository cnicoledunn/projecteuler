#!/usr/bin/env python3
from math import sqrt
from typing import List

class TriangleGenerator:
    def __init__(self) -> None:
        self.num_generated = 1
        self.trinum = 0

    def get_next(self) -> int:
        self.trinum += self.num_generated
        self.num_generated += 1
        return self.trinum

def get_divisors(trinumber:int) -> List[int]:
    divisors=[trinumber]
    for x in range(1, int(sqrt(trinumber))+1):
        if trinumber%x==0:
            divisors.append(x)
            divisors.append(trinumber//x)
    return divisors

tg = TriangleGenerator()
while True:
    temp = tg.get_next()
    if len(get_divisors(temp))>=500:
        print(temp)
        break



