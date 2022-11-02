'''
많은 회사가 모여있음
1-N 번까지 회사 존재
양방향 이동 가능
1 -> K(소개팅) -> X(물건팔이)
최소시간 계산하기
연결된 회사라면 이동하는데 1만큼 시간으로 이동
'''
import sys
input=sys.stdin.readline
n,m = map(int,input().split()) # n : 회사의 개수, m : 경로의 개수
INF = 1e9
company = [[INF]*(n) for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    company[a-1][b-1]=1     #연결된 곳은 1시간 걸림. - 1로 배치
    company[b-1][a-1]=1

x,k = map(int,input().split()) # 가야할 회사 위치

for i in range(n):
    company[i][i]=0 # 본인 회사는 0 처리

for h in range(n):          # 플로이드워셜 알고리즘 수행 (이동하는 곳이 있다면 값을 더해준다)
    for i in range(n):
        for j in range(n):
            company[i][j] = min(company[i][j], company[i][h]+company[h][j])

if company[k-1][x-1]==INF:      # 만일 값이 무한이라면 갈 수 없다는 뜻, -1출력
    print(-1)
else :
    print(company[1][k-1]+company[k-1][x-1]) # 1번회사에서 출발해서 k를 거쳐 x로 가므로 해당 값을 모두 더함



