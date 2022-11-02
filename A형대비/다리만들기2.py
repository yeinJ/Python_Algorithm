'''
이차원 격자
상하좌우로 붙어있는 덩어리 : 섬
다리의 길이는 2이상
모든 섬을 연결하는 다리 길이의 최솟값 구하기, 불가능하다면 -1
'''

# 섬에 번호 붙여주기
def find_start():
    global cnt
    for i in range(N):
        for j in range(M):
            if island[i][j]==1:
                cnt += 1
                return i,j
    return 's','s'

di = [0,1,0,-1]
dj = [1,0,1,-1]
def bfs(i,j,cnt):
    island[i][j]=cnt
    for h in range(4):
        ni = i+di[h]
        nj = j+dj[h]
        if 0<=ni<N and 0<=nj<M and island[ni][nj]==1:
            island[ni][nj]=cnt
            bfs(ni,nj,cnt)



N,M = map(int,input().split())
island = [list(map(int,input().split())) for _ in range(N)]
cnt = 1
while True:
    i,j=find_start()
    if i=='s':
        break
    bfs(i,j,cnt)
island_cnt = cnt-1 # 섬의 개수
for h in range(2,cnt+1):
    for i in range(N):
        for j in range(M):
            if island[i][j]==h:
                direction = [[],[],[],[]]
                for k in range(4):
                    length = 0
                    ni = i+di[k]
                    nj = j+dj[k]
                    while 0<=ni<N and 0<=nj<M and island[ni][nj]==0:
                        length += 1
                        island[ni][nj]=1
                        ni += di[k]
                        nj += dj[k]
                    if length < 2:
                        continue
                    else :
                        if direction[k]==[]:
                            direction[k]=(length,island[ni][nj])
                        else :
                            if island[ni][nj]!=direction[k][1]:
                                direction[k].append((length,island[ni]))
                            else :
                                if direction[k][0]>length:
                                    direction[k]=(length,island[ni][nj])
                print(direction)





print(island)

