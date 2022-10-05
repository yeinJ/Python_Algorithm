import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y,c = map(int,input().split())
    graph[x].append((y,c))
start,end = map(int,input().split())
distance = [INF]*(n+1)
path = [[] for _ in range(n+1)]
path[start].append(start)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1] # i[1]은 현재 i[0]에 저장된 비용
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
                path[i[0]] = []
                for p in path[now]:
                    path[i[0]].append(p)
                path[i[0]].append(i[0])


dijkstra(start)
print(distance[end])
print(len(path[end]))
print(*path[end])
