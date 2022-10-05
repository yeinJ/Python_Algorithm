def dfs(n):
    global cnt
    visited[n]=1
    for i in line[n]:
        if not visited[i]:
            cnt += 1        # 방문하면 cnt+1
            dfs(i)

computer = int(input())
node = int(input())
line = [[] for _ in range(101)]
cnt = 0
for _ in range(node):
    a,b = map(int,input().split())
    line[a].append(b)
    line[b].append(a)
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수
# 1번과 연결된 모든 경우 출력해야 함 - 즉, dfs 사용
visited = [0]*(101)
# 단, 컴퓨터에 적힌 숫자를 모르므로 어떤 장소에 visited될 지 모름
# 따라서 컴퓨터 숫자의 최대 수인 100 까지 visited 잡아줌

dfs(1)
print(cnt)
