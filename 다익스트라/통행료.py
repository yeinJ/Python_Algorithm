'''
최소한의 비용으로 이동할 수 있는 경로 구하기
첫 해의 최소 통행료와
1-k년 후의 세금이 올랐을 때 최소 통행료 출력하기
최소비용으로 이동할 수 있는 경로수와 통행료 구하기
해당 경로수만큼 물가상승*경로수 값을 더해주기
'''
import sys
import heapq
input = sys.stdin.readline
n,m,k = map(int,input().split())
# n : 도시의 수, m : 고속도로 수, k : 햇수
start,end = map(int,input().split())
# 도시 a와 도시 b
graph = [[] for _ in range(n+1)]
INF = 1e9
for _ in range(m):
    f,t,c = map(int,input().split())
    graph[f].append([t,c])      # 통로에 값이 주어지면 양쪽 방향으로 이어져있다는 의미
    graph[t].append([f,c])
year = [0]+[int(input()) for _ in range(k)]

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) # 처음 시작 값 넣기, 비용은 0으로 측정
    distance[start]=0           # distance[start]는 시작 위치이므로 0으로 설정
    while q :
        dist,now = heapq.heappop(q) # 가장 짧은 값 뽑기
        if distance[now]<dist:      # distance에 기록된 값보다 dist 값이 크다면 건너뜀
            continue
        for i in graph[now]:
            cost = dist+i[1]
            # 현재 노드를 거쳐서 다음 노드로 갈때, 값이 더 작다면
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

for i in range(k+1):
    distance=[INF]*(n+1) # for문 돌릴때마다 써야함
    for j in range(n+1):
        for h in range(len(graph[j])):      # graph내에서 [1] 값은 비용 값임
            graph[j][h][1]+=year[i]         # year가 증가할때마다 값을 더해주기
    dijkstra(start)                         # 더해준 값에서 다익스트라 실행시키고, 최소비용찾기
    print(distance[end])                    # end 값 위치에서의 최소값 print

