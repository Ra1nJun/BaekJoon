# 2606 - 바이러스 - silver 3
from collections import deque

N = int(input())
com = [[] for _ in range(N)]
chk = [False for _ in range(N)]

M = int(input())
for i in range(M):
    a, b = map(int, input().split())
    com[a-1].append(b-1)
    com[b-1].append(a-1)

q = deque([0])
cnt = -1
chk[0] = True
while q:
    cnt += 1
    worm = q.popleft()
    
    for c in com[worm]:
        if chk[c] == False:
            q.append(c)
            chk[c] = True

print(cnt)