# 1105 - 팔 - silver 1
L, R = map(str, input().split())

if len(R) != len(L): # 자릿수가 다르다면 8을 포함하지 않는 수가 존재
    print(0)
else:
    arr_L = list(L)
    arr_R = list(R)
    cnt = 0
    for i in range(len(arr_L)): # 동일한 자릿수의 8의 개수만이 요점
        if arr_L[i] != arr_R[i]:
            break
        if arr_L[i] == '8':
            cnt += 1
    print(cnt)