# 1707 - 이분 그래프- gold 4
# AI 도움 받음 : 재귀 함수에서 자식이 부모에게 return값이 전해질 수 있도록 수정
import sys
sys.setrecursionlimit(10**6)

def dfs(node, group):
    group ^= 1
    if group == 1:
        red_group[node] = True
    visited[node] = True
    for k in graph[node]:
        if visited[k] == False:
            if not dfs(k, group):
                return False
        else:
            if red_group[node] == red_group[k]:
                return False
    return True

K = int(sys.stdin.readline())
result = [True for _ in range(K)]
for k in range(K):
    V, E = map(int, sys.stdin.readline().split())
    visited = [False] * V
    red_group = [False] * V
    graph = [[] for _ in range(V)]
    for i in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    for i in range(V):
        if visited[i] == False:
            if not dfs(i, 0):
                result[k] = False
                break

for r in result:
    if r:
        print("YES")
    else:
        print("NO")