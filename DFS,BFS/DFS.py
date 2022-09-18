# 깊이우선탐색
'''
소요시간 O(N)
그래프의 깊은 부분을 우선적으로 탐색
그래프 표현 방법
1. 인접행렬방식
2. 인접리스트방식
인접리스트 방식의 경우 상대적으로 메모리 낭비가 적다. 불필요햔 값을 넣지 않기에
단, 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느리다.
'''
def dfs(graph,v,visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False]*9
dfs(graph,1,visited)