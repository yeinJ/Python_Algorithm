N,M,K = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
next = [[0]*N for _ in range(N)]
ope = []
for _ in range(K):
    r,c,s = map(int,input().split())
    r1,c1 = r-(s+1),c-(s+1)
    r2,c2 = r+(s-1),c+(s-1)
    ope.append([r1,c1,r2,c2])


di = [0,1,0,-1]
dj = [1,0,-1,0]

