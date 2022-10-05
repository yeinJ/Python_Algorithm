from collections import deque
t=0
di = [0,1,0,-1]
dj = [1,0,-1,0]
while True :
    t += 1
    N = int(input())
    if N == 0 :         # N 이 0 일 경우 반복문 종료
        break
    cage = [list(map(int,input().split())) for _ in range(N)]       # 각 리스트 담기
    visited = [[1e9]*N for _ in range(N)]                           # visit값 담기 N*N
    q=deque()
    q.append((0,0))
    visited[0][0]=cage[0][0]                                        # 처음 visit값은 cage값과 같게
    while q:
        i,j=q.popleft()                                             # i,j 값 q에 담고 돌리기
        for h in range(4):
            ni = i + di[h]
            nj = j + dj[h]
            if 0<=ni<N and 0<=nj<N and visited[ni][nj]>visited[i][j]+cage[ni][nj]:
                visited[ni][nj]=visited[i][j]+cage[ni][nj]              # 만약 현재 사용되는 visited값보다 지금 들어오는 값의 cage+visit값이 더 작으면
                q.append((ni,nj))                                       # 바꿔주고, q에 담아주기
    print(f'Problem {t}: {visited[N-1][N-1]}')



