# 7576 - 토마토 - gold 5
from collections import deque
import sys

M, N = map(int, sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dy = [-1,1,0,0]
dx = [0,0,1,-1]
q = deque([])

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            q.append((i,j,0))

while q:
    ey, ex, day = q.popleft()
    for i in range(4):
        ny = ey + dy[i]
        nx = ex + dx[i]
        if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 0:
            q.append((ny,nx,day + 1))
            board[ny][nx] = 1

for i in range(N):
    if 0 in board[i]:
        day = -1
        break

print(day)