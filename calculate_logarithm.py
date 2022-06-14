from math import log, e

number = int(input())
base = input()

if base == 'natural':
    print(f"{log(10, e):.2f}")
else:
    num = int(base)
    print(f"{log(10, num):.2f}")