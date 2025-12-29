# 1260 - DFS와 BFS - silver 2
from collections import deque
N, M, V = map(int, input().split())

graph = [[] for _ in range(N)]
chk = [False for _ in range(N)]
result = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
for i in range(N):
    graph[i] = sorted(graph[i])


def dfs(node):
    chk[node] = True
    result.append(node+1)

    for n in graph[node]:
        if chk[n] == False:
            dfs(n)

def bfs(start):
    queue = deque([start])
    chk[start] = True

    while queue:
        node = queue.popleft()
        result.append(node+1)

        for n in graph[node]:
            if chk[n] == False:
                chk[n] = True
                queue.append(n)

dfs(V-1)
print(*result)

chk = [False for _ in range(N)]
result = []
bfs(V-1)
print(*result)