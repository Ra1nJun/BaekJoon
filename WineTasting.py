# 2156 - 포도주 시식 - silver 1
import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]

if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[1]+arr[0])
else:
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = arr[1]+arr[0]
    dp[2] = max(arr[2]+max(arr[1],arr[0]), dp[1])
    for i in range(3,n):
        dp[i] = max(arr[i]+max(arr[i-1]+dp[i-3],dp[i-2]), dp[i-1])

    print(dp[n-1])