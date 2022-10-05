'''
N*M 직사각형을 만들고 값을 받아 해당하는 위치에 1을 표시한다.
0 주위의 모든 좌표를 다 표시할 시, 시작 점을 1이 아닌 곳으로 재배치한다.
정렬은 오름차순으로 정렬
'''
def find_start():
    for i in range(M):
        for j in range(N):
            if graph[i][j]==0:
                return i,j
    return 'no'

def bfs(i,j):
    global cnt,a_list
    graph[i][j]=1
    for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
        ni,nj = i+di,j+dj
        if 0<=ni<N and 0<=nj<N and graph[ni][nj]==0:
            cnt += 1
            graph[ni][nj]=1
            if bfs(ni,nj):

            else :
                a_list.append(cnt)
                cnt = 0



M,N,K = map(int,input().split())
graph=[[0]*N for _ in range(M)]
visited = [[0]*N for _ in range(N)]
a_list = []
cnt= 1
for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j]=1
while True :
    if find_start()=='no':
        break
    bfs(find_start()[0],find_start()[1])
print(a_list)


