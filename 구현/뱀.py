# N = int(input())
# arr= [[0]*N for _ in range(N)]
# ni,nj=1,1 # 뱀의 시작
# cnt,n = 0,0
# K = int(input())
# apple = [list(map(int,input().split())) for _ in range(K)]
# L = int(input())
# road = [list(input().split()) for _ in range(L)]
# di,dj = 0,1
# snake = [[ni,nj]] # 뱀 길이 담을 리스트
#
# for h in range(L):
#     road[0][0]=int(road[0][0])-1
#     for k in range(1,int(road[h][0])+1):
#         ni += di
#         nj += dj
#         if [ni, nj] in snake:       # snake안에 있으면 서로 부딪힌 것이므로 멈춰준다.
#             n = 5000
#             break
#         if 0<ni<=N and 0<nj<=N:
#             cnt += 1
#             print(cnt,ni,nj,snake)
#             snake.append([ni, nj])  # 뱀의 길이를 담아준다.
#             if [nj,ni] in apple:
#                 continue            # 사과를 먹으면 빼주지 않는다.
#             else :                  # 사과가 없으면 빼준다.
#                 snake.pop(0)
#         else :
#             n = 5000
#             break                   # 범위 밖으로 넘어갔으므로 멈춰준다.
#
#         if k == int(road[h][0]):
#             if di == 1 or di == -1:
#                     if road[h][1]=='D': # 방향이 세로일 경우
#                         dj = -di        # 왼쪽은 대칭이 되고 오른쪽 방향은 -1 해준다.
#                         di = 0
#                     else :
#                         dj = di
#                         di = 0
#             else :
#                 if road[h][1]=='D':     # 방향이 가로일 경우
#                     di = dj             # 오른쪽은 대칭이 되고 왼쪽은 -1 해준다.
#                     dj = 0
#                 else :
#                     di = -dj
#                     dj = 0
#
#     if n== 5000:
#         break
#
# print(cnt)
#
n = int(input())
k = int(input())
apple = [list(map(int, input().split())) for _ in range(k)]
L = int(input())
turn = [list(map(str, input().split())) for _ in range(L)]
dx =[1, 0, -1, 0]#처음에 무조건 오른쪽으로 시작 그래서 i = 3
dy =[0,-1, 0, 1] #오른쪽이면(D)dx[0]부터 왼쪽으면 dx[2]
snake = [[1,1]] #처음 칸에 뱀이 들어있다고 가정. 큐처럼 사용
arr = [[0]*(n+1) for _ in range(n+1)] #1,1 부터 시작이라 한줄씩 더 늘림
i = 3
ni, nj = 1,1 #1,1부터 시작
cnt = 0
while(True):
    if cnt == 0: #처음 시작일때 빈 arr에 1을 넣어주기 위함.
        arr[ni][nj] = 1
    cnt += 1
    ni = ni + dx[i]
    nj = nj + dy[i]
    if 1 <= ni<n and 1 <= nj < n: #칸 밖으로 벗어날때 끝
        if arr[ni][nj] != 0: # 1과 부딪힐때 끝
            break
    else:
        break
    arr[ni][nj] = 1 # 배열에 뱀 표시
    snake.append([ni,nj]) #뱀 길이 및 큐처럼 쓰기 위함.
    if [ni,nj] in apple: #사과자리를 통과하면 pop안하고 그대로 길이 유지
        continue
    else:
        cut = snake.pop(0) #길이 줄이고 꼬리칸을 0으로
        arr[cut[0]][cut[1]] = 0
    if turn == []: #turn 리스트가 비어서 indexerror났음. 방지용
        continue
    elif cnt == int(turn[0][0]): #초와 회전초가 같으면
        if turn[0][1] == 'D': #오른쪽일때
            i += 1 #방향판 우회전
            if i == 4:# i가 밖으로 벗어나면 다시 0으로
                i = 0
        elif turn[0][1] =='L':
            i -= 1
            if i == -1:
                i = 3
        turn.pop(0) #다 쓴 turn 삭제
print(cnt)