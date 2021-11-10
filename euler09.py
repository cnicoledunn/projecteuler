#!/usr/bin/env python3

def printing(a,b,c):
    print (a)
    print (b)
    print (c)
    print (a*b*c)

for c in range(0, 1001):
    for b in range (0, c):
        for a in range (0, b):
            if c**2 == a**2 + b**2:
                if a+b+c==1000:
                    printing(a,b,c)


