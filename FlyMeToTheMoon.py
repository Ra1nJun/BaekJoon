# 1011 - Fly me to the Alpha Centauri - gold 5
import math

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    dis = y-x
    n=int(math.sqrt(dis)) # sqrt쓰기 전에는 n=1 (361ms), 후에는 (36ms)
    while (n*(n+1) < dis):
        n += 1

    if (n*(n+1) - n < dis):
        print(2*n)
    else:
        print(2*n-1)