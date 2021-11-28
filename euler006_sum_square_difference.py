#!/usr/bin/env python3

s = range(1, 101)

def sumsquares(s):
    y = 0
    for i in s:
        y+=i**2
    return y

def sumsquares(s):
    return sum([i**2 for i in s])

def squaresum(s):
    x = 0
    for i in s:
        x = x + i
    return x**2

def squaresum(s):
    x = 0
    for i in s:
        x+=i
    return x**2

def squaresum(s):
    return sum(s)**2

def difference(s):
    return (squaresum(s) - sumsquares(s))

print (difference(s))
