#1238 백준
N,M,X = map(int,input().split())
d=[[] for _ in range(N+1)]
for _ in range(M):
    S,E,T = map(int,input().split())
    d[S].append([E,T])
print(d)
