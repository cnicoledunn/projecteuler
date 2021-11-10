#!/usr/bin/env python3

s = set()

for x in range(100, 999):
    for y in range (100, 999):
        s.add(x*y)
s = sorted(list(s),reverse=True)
for i in s:
    if str(i) == str(i)[::-1]:
        print (i)
        break







