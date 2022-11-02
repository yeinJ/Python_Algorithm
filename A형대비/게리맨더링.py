# 17471
'''
두 선거구로 나뉠 때 각각의 구는서로 연결되어있어야 함
공평하게 나누기 위해 두 선서구 인구의 차이 최소화
인구차이의 최솟값을 구하기
셋째줄부터 N개의 줄에 각 구역과 인접한 정보가 주어짐


'''
def bfs(v):
    global visited
    #print(f'{v}v')
    visited[v] = 1
    for h in link[v]:
        print(h)
        if visited[h]==0:
            bfs(h)

def find_friend():
    global gu1,gu2





import sys
from itertools import combinations
input = sys.stdin.readline
N = int(input())
population = [0]+list(map(int,input().split()))
link=[[]]
visited = [0]*(N+1)
min_po = 1e9
gu1 = {}
gu2 = {}
cnt = 0
for k in range(1,N+1):
    e=list(map(int,input().split()))
    if e[0]!=0:
        link.append(e[1:])
    else :
        cnt += 1
        gu1 = population[k]
        gu2 = sum(population)-population[k]
        min_po = gu2 - gu1
        if cnt > 1 and N>2:
            min_po = -1
            break


if min_po != 1e9:
    print(min_po)
else :








