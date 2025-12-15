# 1092 - 배 - gold 5
# AI 도움 받음 : 각 크레인의 포인터를 따로 만들어서 들 수 없는 화물은 넘기고 찾기 시작함
N = int(input())
N_arr = list(map(int, input().split()))
M = int(input())
M_arr = list(map(int, input().split()))

N_arr.sort(reverse=True)
M_arr.sort(reverse=True)

if M_arr[0] > N_arr[0]:
    print(-1)
else:
    moved = [False] * M
    cnt = M
    time = 0
    p = [0] * N
    
    while cnt > 0:
        time += 1
        for i in range(N):
            j = p[i] 
            while j < M:
                if not moved[j] and N_arr[i] >= M_arr[j]:
                    moved[j] = True
                    cnt -= 1
                    p[i] = j + 1
                    break
                j += 1
            if j == M:
                p[i] = j

    print(time)