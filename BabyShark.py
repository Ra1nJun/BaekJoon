# 16236 - 아기 상어 - gold 3
# AI 도움 받음 : 먹을 물고기 찾는 로직의 위치
import sys
from collections import deque

N = int(sys.stdin.readline())
fishTank = []

for i in range(N):
    l = list(map(int, sys.stdin.readline().split()))
    for j in range(len(l)):
        if l[j] == 9:
            sharkY, sharkX = i,j
    fishTank.append(l)
fishTank[sharkY][sharkX] = 0

dy = [1,-1,0,0]
dx = [0,0,1,-1]
size = 2
ate = 0
total = 0

def bfs(y, x):
    q = deque([(0,y,x)])
    chk = [[False]* N for _ in range(N) ]
    chk[y][x] = True
    fishLi = []
    while q:
        dis, ey, ex = q.popleft()
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if 0 <= ny < N and 0 <= nx < N and fishTank[ny][nx] <= size and chk[ny][nx] == False:
                chk[ny][nx] = True
                if 0 < fishTank[ny][nx] < size:
                    fishLi.append((dis+1, ny, nx))
                else:
                    q.append((dis+1, ny, nx))
                
    return fishLi

while True:
    meal = bfs(sharkY, sharkX)
    if not meal:
        break

    meal = sorted(meal)
    dis, my, mx = meal[0]
    total += dis
    fishTank[my][mx] = 0
    sharkY, sharkX = my, mx
    ate += 1

    if ate == size:
        size += 1
        ate = 0

print(total)