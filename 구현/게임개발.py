# 게임 개발
# 게임 캐릭터는 항상 육지에서 시작한다
# 주변 칸이 바다이거나 뒤로 갈 수 없는 경우 멈춘다.
# 0 : 육지, 1 : 바다
# 구해야 하는 값 : 캐릭터가 방문한 칸 수
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1
N,M = map(int,input().split())
A,B,d = map(int,input().split()) # 시작좌표 AB, 바라보는 방향 d
arr = [list(map(int,input().split())) for _ in range(N)]
arr[A][B]+=1
# si,sj=시작순서 북,동,남,서 / 왼쪽으로 돌 때 이동 순서 (북 서 남 동)
si = [-1,0,1,0]
sj = [0,1,0,-1]
cnt,con = 1,0 # 처음 시작의 좌표 포함해줌
k=d+1
while True :
    ni = A+si[4-k]
    nj = B+sj[4-k]
    if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
        arr[ni][nj]=1
        A,B = ni,nj
        cnt += 1
        con = 0
        k += 1
    else :
        con += 1
        k += 1
    if k == 5:          # k 가 4 이상일 시, 초기화
        k = 1
    if con == 4:        # 상하좌우 모두 막혔을 시
        ni = A - si[4-k]
        nj = B - sj[4-k]
        if arr[ni][nj] == 0:    # 주위에 0이 하나라도 있을 경우
            A=ni
            B=nj
        else :          # 바다에 접근할 경우
            break
        con = 0
print(cnt)




# N,M = list(map(int, input().split()))
# a, b, head = list(map(int, input().split()))
# arr = [list(map(int, input().split())) for _ in range(N)]
# compass = [0,1,2,3] #북 동 남 서
# di = [[-1,0],[0,1],[1,0],[0,-1]]
# cnt = 0
# def dfs(a,b):
#     arr[a][b]=1
#     global cnt
#     cnt += 1
#     for i in range(4): #네방향
#         ni = a+di[i][0]
#         nj = b+di[i][1]
#         if 0<= ni < N and 0<= nj < N:
#             if arr[ni][nj]==0:
#                 dfs(ni,nj)
# dfs(a,b)
# print(cnt)


N, M = map(int, input().split())    # 열크기, 행크기
y,x,d = map(int, input().split())   # 행번호, 열번호, 방향

board = [list(map(int, input().split())) for _ in range(N)] # 게임 맵
di = [-1,0,1,0] # 북동남서
dj = [0,1,0,-1]
cnt = 0
check = 0                           # 4에 도달하면 매뉴얼 3실행
board[y][x] = 3                     # 이동했던 길이라면, 3으로 표시(시작점)
while True:                         # 시뮬실행
    d -= 1                          # 시계방향 회전
    if d == -1:                     # 북에서 회전시 서(인덱스 마지막)
        d = 3
    ni = y + di[d]
    nj = x + dj[d]
    if 0<= ni < N and 0<= nj < M:   # 회전한곳이 게임맵 안인가?
        if board[ni][nj] == 0:      # 해당 장소가 육지라면 이동해라
            y,x = ni, nj
            check = 0
            cnt += 1
            board[ni][nj] = 3
        else:
            check += 1
    else:
        check += 1

    if check == 4:                  # 주변이 이동할 수 없다면,
        d -= 2                      # 뒤로 돌아라.
        if d == -1:
            d = 3
        ni = y + di[d]
        nj = x + dj[d]
        if 0 <= ni < N and 0 <= nj < M: # 뒤에가 이동할 수 있는 길이 있는가?
            if board[ni][nj] == 3:      # 뒤로 이동해라
                y, x = ni, nj
                check = 0
                cnt += 1
                board[ni][nj] = 3
                d -= 2
                if d < 0:
                    d += 4
            else:                       # 만약 뒤에가 범위밖이거나 바다(1)라면 종료
                break
        else:
            break

print(cnt)

