# 2563 - 색종이 - silver 5
# AI 도움 받음 : 겹치는 부분을 빼는 것이 아닌 색이 칠해진 곳을 더하는 문제
N = int(input())
area = set()

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            area.add((i, j))

print(len(area))