# 1987 - 알파벳 - gold 4
# AI 도움 받음 : 문자열을 추가하고 in연산자를 통해 체크 -> 알파벳 개수만큼 bool리스트를 만들어 체크
import sys

R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline())[:-1] for _ in range(R)]
chk = [False] * 26

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
res = 0

def dfs(y, x, cnt):
    global res
    res = max(res, cnt)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < R and 0 <= nx < C:
            idx = ord(board[ny][nx])-ord('A')
            if chk[idx] == False:
                chk[idx] = True
                dfs(ny,nx,cnt+1)
                chk[idx] = False

chk[ord(board[0][0])-ord('A')] = True
dfs(0,0,1)
print(res)