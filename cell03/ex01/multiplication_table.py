#!/usr/bin/env python
number = int(input("multiplication table: "))

print(f"Multiplication table for {number}:")

for i in range(1, 26):
    result = number * i

    print(f"{number} x {i} = {result}")
