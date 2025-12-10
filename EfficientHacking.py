# 1325 - 효율적인 해킹 - silver 1
# AI 도움 받음 : DFS(깊이 우선:스택)를 사용하여 시간 초과 -> BFS(너비 우선:큐)로 변경
from collections import deque # queue가 아닌 deque를 쓰는 이유 : 큐는 멀티스레드 환경에서도 안전하도록 락이 걸려 데크보다 느림. + 리스트는 O(N), 데크는 O(1)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

def bfs(start):
    visited = [False] * (N+1)
    visited[start] = True
    q = deque([start])
    cnt = 1
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                cnt += 1
                q.append(nxt)
    return cnt

res = []
max_hack = 0

for i in range(1, N+1):
    cnt = bfs(i)
    if cnt > max_hack:
        max_hack = cnt
        res = [i]
    elif cnt == max_hack:
        res.append(i)

print(*res)