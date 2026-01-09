# 2839 - 설탕 배달 - silver 4
import sys

N = int(sys.stdin.readline())

k = N//5
r = N%5
result = -1

while(k>=0):
    if r%3 == 0:
        result = k + r//3
        break
    k -= 1
    r += 5

print(result)