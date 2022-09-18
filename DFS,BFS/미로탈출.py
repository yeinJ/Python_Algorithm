'''
동빈이 N*M 크기의 직사각형 형태 미로에 갇혀 있음
동빈 위치 (1,1)
미로 출구 (N,M)
동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수 구하기
'''

N, M = map(int,input().split()) # N = 세로 M = 가로
miro = [list(map(int,input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

di = [-1,0,1,0]     # 상 우 하 좌
dj = [0,1,0,-1]

def bfs(i,j):
    nt = 1
    q = [(i,j)]     # 시작점 담기
    visited[i][j]=1 # 시작점 방문했다고 표시
    while q :       #  q가 존재하면 while을 계속 돌린다.
        nt += 1
        for h in range(len(q)):     # q에 담아진 리스트 다 꺼내기 (길은 두가지가 될 수 있기에)
            ei,ej = q.pop(0)
            for k in range(4):
                ni = ei+di[k]
                nj = ej+dj[k]
                if 0<=ni<N and 0<=nj<M and miro[ni][nj]==1 and visited[ni][nj]==0:
                    visited[ni][nj]=nt
                    q.append((ni,nj))   # 4번 회전할때 방향 여러개면 다 담아주고 위에 for문에서 다 빼주기

    return visited[N-1][M-1]

print(bfs(0,0))



