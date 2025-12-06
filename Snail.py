# 2869 - 달팽이는 올라가고 싶다 - bronze 1
import math

A, B, V = map(int, input().split())

if A == V:
    result = 1
else:
    day = math.ceil((V - A) / (A - B))
    result = day + 1

print(result)