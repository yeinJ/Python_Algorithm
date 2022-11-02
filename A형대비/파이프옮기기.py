'''
파이프는 대각선으로 갈 때 무조건 한칸을 옮기고 나서 대각선으로 갈지를 고민함
따라서 처음 칸에서 한칸 간 후, 대각선으로 밀지 안 밀지를 생각하면 됨
대각선에서는 가로, 세로 파트를 모두 포함해주기 때문에 해당 조건을 포함해야함
재귀로 풀음. pypy로 통과 메모리 120000... 시간 0.96초(아슬아슬)

'''

def move_pipe(a1, b1, a2, b2):      # 파이프의 앞, 뒤 방향 설정
    global cnt
    if (a2,b2)==(eni,enj):
        cnt += 1
    if (a2 - a1, b2 - b1) == (0, 1):                # 파이프의 뒤에서 앞을 뺀 값이 방향 -> 해당 방향에 따라 조건 따로
        ni = a2
        nj = b2 + 1
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:        # 파이프 방향이 가로인 경우, 가로로 가는 경우를 구하고
            move_pipe(a2, b2, ni, nj)                               # 해당 경우에서 대각선을 갈 수 있는지 경우의 수 구함
            if 0<=ni+1<N and arr[ni + 1][nj] == 0 and arr[ni + 1][nj - 1] == 0:
                move_pipe(a2, b2, ni + 1, nj)
        else :
            return
    elif (a2-a1,b2-b1)==(1,0):
        ni = a2 + 1
        nj = b2
        if 0<= ni < N and 0<=nj < N and arr[ni][nj]==0:
            move_pipe(a2,b2,ni,nj)
            if 0<=nj+1<N and arr[ni][nj+1]==0 and arr[ni-1][nj+1]==0:
                move_pipe(a2,b2,ni,nj+1)
    else :
        if 0<=a2+1<N and arr[a2+1][b2]==0:                          # 파이프가 대각선인 경우 오른쪽, 아래쪽이 0인지 확인해주고 0이 아니면 재귀 돌리지 x
            move_pipe(a2,b2,a2+1,b2)
        if 0<=b2+1<N and arr[a2][b2+1]==0:
            move_pipe(a2,b2,a2,b2+1)
        if 0<=a2+1<N and 0<=b2+1<N and arr[a2+1][b2+1]==0 and arr[a2][b2+1]==0 and arr[a2+1][b2]==0 :
            move_pipe(a2,b2,a2+1,b2+1)




N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
eni, enj = N - 1, N - 1
cnt = 0
move_pipe(0,0,0,1)
print(cnt)

'''
숏코딩 코드
'''
n = int(input())
l = [list(map(int,input().split())) for i in range(n)]
s = [[[0,0,0][:]for _ in range(n)] for i in range(n)]
s[0][1][0]=1
for i in range(n):
    for j in range(n):
        if l[i][j]==0:
            s[i][j][0]+=sum(s[i][j-1][:2])
            s[i][j][2]+=sum(s[i-1][j][1:])
            if j and l[i-1][j]+l[i][j-1]==0:s[i][j][1]=sum(s[i-1][j-1])
print(sum(s[i][j]))

'''
'''
"""
0, 가로일때: 대각선/ 가로
1, 세로일때: 대각선/ 세로
2, 대각선일때: 대각선/ 가로/ 세로
1은 벽
3은 파이프

dfs방식 : 63% 시간초과    (pypy는 통과)
dp 구현
"""

import sys
N = int(input())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp = [[[0]*N for _ in range(N)] for _ in range(3)]    # dp[0] 가로이동기록, dp[1] 세로이동기록, dp[2] 대각선이동기록

for i in range(N):          # 첫줄은 가로로만 이동이 가능하다.
    if board[0][i] == 0:
        dp[0][0][i] = 1
    else:
        break

for i in range(1,N):        # 첫줄은 위에서 이미 설정함.
    for j in range(2,N):    # 최초에 가로로 설정했기때문에 세로0과 세로1은 설정할 수 없음.
        # 대각선 먼저 체크를 해보겠습니다.

        # 현재위치가 대각선이라면, 대각선-대각선, 가로-대각선, 세로-대각선의 합이다.
        if board[i][j] == 0 and board[i-1][j] == 0 and board[i][j-1] == 0:
            dp[2][i][j] = dp[2][i-1][j-1] + dp[1][i-1][j-1] + dp[0][i-1][j-1]

        # 가로 세로를 확인하겠습니다.
        if board[i][j] == 0:
            # 현재위치가 세로일경우, 대각선에서 세로로 오는경우 + 세로에서 세로로 오는경우
            dp[1][i][j] = dp[2][i-1][j] + dp[1][i-1][j]
            # 현재위치가 가로일경우, 대각선에서 가로로 오는경우 + 가로에서 가로로 오는경우
            dp[0][i][j] = dp[2][i][j-1] + dp[0][i][j-1]

print(dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1])