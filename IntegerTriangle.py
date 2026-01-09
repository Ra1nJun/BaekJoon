# 1932 - 정수 삼각형 - silver 1
# Top-Down 방식보다 Bottom-Up 방식이 메모리 효율성에서 장점이 있다
import sys

n = int(sys.stdin.readline())
tri = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n-2,-1,-1):
    for j in range(i+1):
        tri[i][j] += max(tri[i+1][j], tri[i+1][j+1])

print(tri[0][0])