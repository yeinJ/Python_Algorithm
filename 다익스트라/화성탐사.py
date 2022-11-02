'''
화성 탐사 기계가 출발 지점에서 목표 지점까지 이동할때, 최적의 경로 찾기
N*N크기의 2차원 공간
화성탐사는 특정한 위치에서 상하좌우 인접한 곳으로 1칸씩 이동할 수 있음
0,0 에서 n-1,n-1까지 이동할때 최소비용 구하기
bfs 써도 될거같은..?
'''
from collections import deque

T = int(input())
for tc in range(T):
    n = int(input())
    account = [list(map(int,input().split())) for _ in range(n)]
    start,end = (0,0),(n-1,n-1)
    direction = deque()
    direction.append(start)
    INF = 1e9
    visited = [[INF]*n for _ in range(n)]
    di,dj=[0,1,0,-1],[1,0,-1,0]
    visited[0][0]=account[0][0]
    while direction:
        i,j=direction.popleft()                     # direction 에서 맨 앞 값 뽑기
        for h in range(4):
            ni = i + di[h]                          # 4방향에서 visited값이 더 크다면 값 바꿔줌, 작다면 냅두기
            nj = j + dj[h]                          # heapq알고리즘 사용 시, 작은 값부터 우선순위로 바꿔주기에 더빨라질듯
            if 0<=ni<n and 0<=nj<n and visited[ni][nj]>visited[i][j]+account[ni][nj]:
                visited[ni][nj]=visited[i][j]+account[ni][nj]
                direction.append((ni,nj))
    print(visited[n-1][n-1])









