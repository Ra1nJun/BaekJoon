# 11726 - 2xn 타일링 - silver 3
import sys

n = int(sys.stdin.readline())

dp = [1] * (n+1)

if n > 1:
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]

print(dp[n]%10007)