# 1715 - 카드 정렬하기 - gold 4
# n == 1 이라면 비교할 필요가 없으므로 0
import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))

if n == 1:
    print(0)
else:
    result = 0
    for _ in range(n-1):
        new = heapq.heappop(heap) + heapq.heappop(heap)
        result += new
        heapq.heappush(heap, new)

    print(result)