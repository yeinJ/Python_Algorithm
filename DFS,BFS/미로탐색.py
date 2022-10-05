#2178
'''
1. di,dj 방향설정
2. 미로를 최소로 탈출하는 방법을 찾아야하기에 bfs 사용
3. 만일 방문하지 않은 곳이고 길(1)에 있으면 해당 좌표를 q에 넣고 방문처리
4. 만일 i,j가 N,M 에 도달할 시, 해당 visited에 적힌 값 출력
'''
di,dj = [0,1,0,-1],[1,0,-1,0]
N , M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
visited=[[0]*M for _ in range(N)]
q = [(0,0)]
visited[0][0]=1
ans = 0
while q:
    i,j = q.pop(0)
    if i==N-1 and j==M-1:
        ans = visited[i][j]
        break
    for a in range(4):
        ni = i+di[a]
        nj = j+dj[a]
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]==1 and visited[ni][nj]==0:
            q.append((ni,nj))
            visited[ni][nj]=visited[i][j]+1
print(ans)





