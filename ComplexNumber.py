# 2667 - 단지번호 붙이기 - silver 1
from collections import deque

N = int(input())
map = [list(map(int, input())) for _ in range(N)]
chk = [[False for _ in range(N)] for _ in range(N)]
result = []

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(y,x):
    q = deque([(y, x)])
    cnt = 0
    chk[y][x] = True
    while q:
        ey, ex = q.popleft()
        cnt += 1
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if  0 <= nx < N and 0 <= ny < N and chk[ny][nx] == False and map[ny][nx] == 1:
                q.append((ny,nx))
                chk[ny][nx] = True
    return cnt

for i in range(N):
    for j in range(N):
        if map[i][j] == 1 and chk[i][j] == False:
            result.append(bfs(i, j))

print(len(result))
result = sorted(result)
for res in result:
    print(res)