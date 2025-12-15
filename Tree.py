# 1068 - 트리 - gold 5
N = int(input())
nodes = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
for node, par in enumerate(nodes):
    graph[par+1].append(node)
d = int(input())

if graph[0][0] == d:
    print(0)
else:
    graph[d+1] = []
    graph = [[node for node in inGraph if node != d] for inGraph in graph]

    stack = []
    i, cnt = 0, 0
    while (True):
        stack += graph[i]
        if not stack:
            cnt += 1
            break
        if not graph[i]:
            cnt += 1
        i = stack.pop() + 1

    print(cnt)