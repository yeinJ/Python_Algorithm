'''
N*M 크기의 얼음 틀이 있다.
for문을 돌려서 visited가 0일 시, index로 저장 - 그곳이 시작점 break
dfs 실행
다시 for문으로 0인곳 찾기, index 설정
dfs 실행
'''
def dfs(visited,v):
    di = [0,1,0,-1]         # 상하좌우 설정
    dj = [1,0,-1,0]
    for h in range(4):      # 만약 상하좌우가 visited되지 않고, 범위도 벗어나지 않았다면
        ni = v[0]+di[h]     # 1로 설정해주고 ni,nj를 재설정해준 뒤
        nj = v[1]+dj[h]     # 재귀로 반복
        if 0<=ni<N and 0<=nj<M and visited[ni][nj]==0:
            visited[ni][nj]=1
            si=(ni,nj)
            dfs(visited,si)


N,M = map(int,input().split())
visited = [list(map(int,input())) for _ in range(N)]
cnt,id = 0,0
while True :                # 빈칸인 곳 찾기 위한 반복문
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                cnt += 1    # for문 실행될 때 빈칸인 곳 발견되면 cnt 1더해주고 break
                id = (i, j)
                visited[i][j] = 1
                break
            else :          # 빈칸이 아무것도 없으면 id= 0으로 반환되어 while문 멈춤
                id = 0
        if id:
            break
    if id == 0:
        break
    dfs(visited,id)


print(cnt)


