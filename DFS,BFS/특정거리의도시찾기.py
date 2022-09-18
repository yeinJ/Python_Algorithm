from collections import deque
import sys
input = sys.stdin.readline          # 받는 값이 1만 이상일 경우 import sys 사용

def dfs(v):
    global visit
    cnt = 0
    visit[v]=99999999999999         # 시작점은 다른 값과 차별되게 매우 큰 값으로 설정
    queue = deque([v])
    while queue:
        cnt += 1
        for h in range(len(queue)): # queque에 담겨진 것은 같은 순서에서의 다른 방향일 뿐이므로 for문을 통해 담겨진 모든 queue를 제거해준다.
            a = queue.popleft()
            for i in road[a]:
                if visit[i] == 0:
                    queue.append(i)
                    visit[i]=cnt


n,m,k,x = map(int,input().split())
road = [[] for _ in range(n+1)]     # 각 방문 노드 담기
visit = [0]*(n+1)                   # 방문했던 곳인지 확인하는 변수
for i in range(m):
    a,b = map(int,input().split())
    road[a].append(b)
dfs(x)
ans = -1
bns = []

for i in range(len(visit)):
    if visit[i]==k:                 # 만약 visit에 최소값이 k인게 존재하면
        ans = 1                     # ans를 1로 바꿔준다.
        bns.append(i)
bns.sort()                          # bns 정렬

if ans == -1:                       # ans가 최소값이 k인게 없다면 -1 그대로일 것이다.
    print(ans)                      # -1을 출력해준다.
else :
    for i in bns:
        print(i)













