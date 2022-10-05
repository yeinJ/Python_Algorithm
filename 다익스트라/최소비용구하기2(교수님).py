from collections import deque
n = int(input())        # 도시
m = int(input())        # 버스
adjM = [[0]*(n+1) for _ in range(n+1)]
visit = [1e9]*(n+1)
node = [-1]*(n+1)
for i in range(m):
    a,b,w = map(int,input().split())
    adjM[a][b]=w
A,B = map(int,input().split())  # 출발도시, 도착도시
# 시작은 A
q = deque()
q.append(A)
visit[A] = 0
while q:
    city=q.popleft()
    for h in range(len(adjM[city])):
        if adjM[city][h]!= 0 and visit[h]>visit[city]+adjM[city][h]:
            visit[h]=visit[city]+adjM[city][h]
            node[h]=city
            q.append(h)

print(visit[B])
k = [B]
while node[B]!=-1 :
    k.append(node[B])
    B = node[B]
print(len(k))
print(*k[::-1])

