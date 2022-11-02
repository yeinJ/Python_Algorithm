def find_max_bong():                        # 봉우리가 가장 최대인 곳의 좌표 구하는 def문
    max_list = []
    for i in range(N):
        for j in range(N):
            if san[i][j]==max_bong:         # 봉우리가 max이면 max_list에 넣어준다.
                max_list.append((i,j))
    return max_list

def bfs(i,j,cnt):                           # 만약 cnt가 long_san보다 크다면 등산로의 최대 길이 변경
    global long_san
    if cnt > long_san:
        long_san = cnt
    for h in range(4):
        ni = i + di[h]
        nj = j + dj[h]
        if 0<=ni<N and 0<=nj<N and san[i][j]>san[ni][nj]:       # san에서 값이 작을때만 bfs 돌리기
            bfs(ni,nj,cnt+1)

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    san = []
    max_bong = 0
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    for _ in range(N):
        k=list(map(int,input().split()))
        san.append(k)
        max_bong = max(max_bong,max(k))         # 봉우리가 가장 높은 봉우리 값 구하기
    max_list=find_max_bong()
    long_san = 0
    for i in range(N):
        for j in range(N):
            for g in range(1, K + 1):           # 최대 K만큼 봉우리를 뺄 수 있으므로 1~K만큼 빼기
                san[i][j] -= g
                for k in max_list:              # def문으로 받아준 max_list 에서 좌표를 뽑아서 bfs에 돌리기
                    if k[0]==i and k[1]==j:
                        continue
                    else:
                        bfs(k[0],k[1],1)        # 첫 시작은 봉우리부터이므로 길이는 1부터 시작이다.
                san[i][j] += g
    print(f'#{tc} {long_san}')






