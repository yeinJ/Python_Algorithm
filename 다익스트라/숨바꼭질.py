'''
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''
import heapq
n,m = map(int,input().split())

graph = [[]*(n+1) for _ in range(n+1)]
start = 1
INF = 1e9
distance = [INF]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dijkstra(start):
    q = []
    # 시작노드에서 시작하기
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보
        dist,now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist :
            continue
        # 현재 노드와 연결된 다른 노드 확인
        for i in graph[now]:
            cost = dist +1
            # 현재 노드에서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i]:
                distance[i]=cost
                heapq.heappush(q,(cost,i))

# 다익스트라 실행
dijkstra(start)
distance[0]=0
cnt = 0
start_num = 0
for i in range(1,n+1):
    if distance[i]==max(distance):
        if start_num==0:
            start_num=i
        cnt +=1
print(start_num,max(distance),cnt)





