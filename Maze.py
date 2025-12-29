# 2178 - 미로 탐색 - silver 1
from collections import deque

N, M = map(int, input().split())
chk = [[False for _ in range(M)] for _ in range(N)]
board = [list(map(int, input())) for _ in range(N)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(y, x):
    cnt = 0
    q = deque([(y,x, 1)])
    chk[y][x] = True
    while q:
        cy, cx, cnt = q.popleft()
        if cy == N-1 and cx == M-1:
            return cnt
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                q.append((ny,nx, cnt+1))
    return -1

result = bfs(0,0)
print(result)