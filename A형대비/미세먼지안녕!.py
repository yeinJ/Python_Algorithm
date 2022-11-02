# 17144
'''
R*C 격자판
공기청정기는 0,0
r,c 칸의 미세먼지 양은 Arc
미세먼지가 있으면 모두 확산됨
Arc/5 만큼 확산
r,c에 남은 미세먼지양 Arc-(Arc/5)*확산된 방향의 개수
T초 후 남은 먼지양
'''
di = [0,-1,0,1]                 # 위쪽 좌표의 공기청정기 방향
dj = [1,0,-1,0]
dmi = [0,1,0,-1]                # 아래 좌표의 공기청정기 방향
dmj = [1,0,-1,0]
R,C,T = map(int,input().split())
Arc = []
air = []
sum_ans = 2

for k in range(R):                      # 데이터를 각각 리스트 형식으로 받기
    arc = []
    rc = list(map(int,input().split()))
    for h in range(C):                  # [[0],[1],[2]]
        if rc[h]==-1:
            air.append((k,h))           # 만약 -1이면 공기청정기이므로 air변수에 담아주기
        arc.append([rc[h]])
    Arc.append(arc)

t=0
while t<T:
    t+=1
    for i in range(R):
        for j in range(C):
            if Arc[i][j][0]!=0 and Arc[i][j][0]!=-1:            # 만약 Arc 리스트에 먼지가 있는 위치라면
                cnt = 0
                dust = Arc[i][j][0] // 5                        # dust //5 해주고
                for h in range(4):
                    ni = i + di[h]
                    nj = j + dj[h]
                    if 0<=ni<R and 0<=nj<C and Arc[ni][nj][0]!=-1:
                        cnt +=1
                        Arc[ni][nj].append(dust)                # dust를 Arc[ni][nj] 리스트 내에 넣어주기
                Arc[i][j][0]=Arc[i][j][0] - cnt*dust            # cnt를 세서 나눠준만큼 Arc에서 빼줌
    for i in range(R):
        for j in range(C):
            Arc[i][j]=[sum(Arc[i][j])]                          #  Arc 에 담긴 list를 sum 해주기
    num = [0]
    for e in range(2):
        si,sj = air[e][0],air[e][1]                             # 공기청정기는 무조건 하나이므로 방향 두개 설정
        if e == 0:
            for h in range(4):
                ni = si + di[h]
                nj = sj + dj[h]
                while 0<=ni<R and 0<=nj<C:
                    if Arc[si][sj][0]==-1:
                        Arc[ni][nj].append(0)
                    else :
                        Arc[ni][nj].append(Arc[si][sj][0])      # 만약 Arc[ni][nj]가 -1이 아니면 그다음 리스트에 저장
                    si, sj = ni, nj
                    if Arc[si][sj][0]==-1:
                        break
                    ni += di[h]
                    nj += dj[h]

        else :
            for h in range(4):                              # 2번째 방향도 같게
                ni = si + dmi[h]
                nj = sj + dmj[h]
                while 0<=ni<R and 0<=nj<C:
                    if Arc[si][sj][0]==-1:
                        Arc[ni][nj].append(0)
                    else :
                        Arc[ni][nj].append(Arc[si][sj][0])
                    si, sj = ni, nj
                    if Arc[si][sj][0]==-1:
                        break
                    ni += dmi[h]
                    nj += dmj[h]

        for i in range(R):                          # 방향 판단이 끝나면 [i][j][0] 이 -1이 아니면 리스트 변경해주기
            for j in range(C):
                if len(Arc[i][j])==2:
                    if Arc[i][j][0]!=-1:
                        Arc[i][j] = [Arc[i][j][1]]
                    else :
                        Arc[i][j] = [Arc[i][j][0]]      # -1이면 그대로
for i in range(R):
    for j in range(C):
        sum_ans+=Arc[i][j][0]                       # 합 구해주기

print(sum_ans)















