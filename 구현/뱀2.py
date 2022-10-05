N = int(input())
K = int(input())
apple = [list(map(int,input().split())) for _ in range(K)]
L = int(input())
road,dir = [0],[]
for _ in range(L):
    x,c = input().split()
    road.append(int(x))         # 몇 칸 이동하는지 road에 넣어주기
    dir.append(c)               # 방향 dir에 넣어주기
road.append(10000)
ni,nj = 1,1
di = [0,1,0,-1]                 # 만약 D로 간다면 +1 L로 간다면 -1
dj = [1,0,-1,0]
start = [[1,1]]                 # 시작은 1,1 로
go,cnt = 0,0                    # go(걸린 시간) cnt (방향)
ans = 0                         # break 걸어주기 위한 변수
for i in range(L+2):            # 총 0, 10000을 넣어주었기에 L+2로
    for j in range(road[i+1]-road[i]):          # i초에서 i+1초 사이
        if i == 0:
            ni=ni + di[cnt]                      # i = 0 일때,
            nj=nj + dj[cnt]
            go += 1
            if 0<ni<N+1 and 0<nj<N+1 and [ni,nj] not in start:    #  범위 안 넘어갈 시
                if [ni,nj] in apple:    # 사과에 있으면 사과 값 지워주고 start에 범위 넣기
                    start.append([ni,nj])
                    apple.remove([ni,nj])
                else :
                    start.pop(0)
                    start.append([ni,nj])
            else :
                ans = 's'
                break

        else :
            if j == 0:
                if dir[i-1] == 'D':
                    cnt = (cnt+1)%4
                else :
                    cnt = (cnt-1)%4
            ni = ni + di[cnt]
            nj = nj + dj[cnt]
            go += 1

            if 0<ni<N+1 and 0<nj<N+1 and [ni,nj] not in start:
                if [ni,nj] in apple:
                    start.append([ni,nj])
                    apple.remove([ni,nj])
                else :
                    start.pop(0)
                    start.append([ni,nj])
            else :
                ans = 's'
                break
    if ans=='s':
        break
print(go)










