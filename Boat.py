# 1092 - 배 - gold 5
import math

N = int(input())
N_arr = list(map(int, input().split()))
M = int(input())
M_arr = list(map(int, input().split()))

N_arr.sort(reverse=True)
M_arr.sort(reverse=True)

if M_arr[0] > N_arr[0]:
    print(-1)

i, j, cnt = 0, 0, 0
while i < N:
    if j >= len(M_arr):
        break
    if N_arr[i] < M_arr[j]:
        j += 1
        continue
    i += 1
    j += 1
    cnt += 1

print(math.ceil(M/cnt))