# 2468 - 안전 영역 - silver 1
import sys
sys.setrecursionlimit(10**6) # AI 도움 받음 : 런타임 에러

N = int(sys.stdin.readline())
m = []
max_h = []
for _ in range(N):
    l = list(map(int, sys.stdin.readline().split()))
    max_h.append(max(l))
    m.append(l)
max_h = max(max_h)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x, h):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N and chk[ny][nx] == False and m[ny][nx] > h:
            chk[ny][nx] = True
            dfs(ny, nx, h)
    return 1

result = []
for k in range(1, max_h):
    chk = [[False]* N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if m[i][j] > k and chk[i][j] == False:
                cnt += dfs(i,j,k)
    result.append(cnt)

if result:
    print(max(result))
else:
    print(1)