N = int(input())
arr= [[0]*N for _ in range(N)]
ni,nj=1,1 # 뱀의 시작
cnt,n = 0,0
K = int(input())
apple = [list(map(int,input().split())) for _ in range(K)]
L = int(input())
road = [list(input().split()) for _ in range(L)]
di,dj = 0,1
snake = [[ni,nj]] # 뱀 길이 담을 리스트

for h in range(L):
    road[0][0]=int(road[0][0])-1
    for k in range(1,int(road[h][0])+1):
        ni += di
        nj += dj
        if [ni, nj] in snake:       # snake안에 있으면 서로 부딪힌 것이므로 멈춰준다.
            n = 5000
            break
        if 0<ni<=N and 0<nj<=N:
            cnt += 1
            print(cnt,ni,nj,snake)
            snake.append([ni, nj])  # 뱀의 길이를 담아준다.
            if [nj,ni] in apple:
                continue            # 사과를 먹으면 빼주지 않는다.
            else :                  # 사과가 없으면 빼준다.
                snake.pop(0)
        else :
            n = 5000
            break                   # 범위 밖으로 넘어갔으므로 멈춰준다.

        if k == int(road[h][0]):
            if di == 1 or di == -1:
                    if road[h][1]=='D': # 방향이 세로일 경우
                        dj = -di        # 왼쪽은 대칭이 되고 오른쪽 방향은 -1 해준다.
                        di = 0
                    else :
                        dj = di
                        di = 0
            else :
                if road[h][1]=='D':     # 방향이 가로일 경우
                    di = dj             # 오른쪽은 대칭이 되고 왼쪽은 -1 해준다.
                    dj = 0
                else :
                    di = -dj
                    dj = 0

    if n== 5000:
        break

print(cnt)

