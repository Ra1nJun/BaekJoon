# 12865 - 평범한 가방 - gold 5
# AI 도움 받음 : 물품의 개수로 dp -> 가방의 무게로 dp
import sys

n, k = map(int, sys.stdin.readline().split())

objects = []
dp = [0] * (k+1)
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    objects.append((w,v))

for w,v in objects:
    for i in range(k,w-1,-1):
        dp[i] = max(dp[i],dp[i-w]+v)
        
print(dp[k])