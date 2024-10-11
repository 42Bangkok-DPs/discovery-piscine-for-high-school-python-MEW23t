#!/usr/bin/env python

array = [2, 8, 9, 48, 8, 22, -12, 2]
plus = set()
for number in array:
    if number + 2 > 5:
        plus.add(number)
pluslist = list(plus)
print("array:", array)
print("Numbers(duplicates):", pluslist)
