'''
각 x좌표마다 누적 합 구하기
계산할때는 세로줄마다 for문을 돌리며 x2-(x1-1)의 값을 구한다
for문이 하나이므로 빅오 표기법상 O(N)
'''
import sys
input=sys.stdin.readline
N,M = map(int,input().split())
table=[list(map(int,input().split())) for _ in range(N)]
num_sum=[[0] for _ in range(N)]
for y in range(N):
    sum_garo = 0
    for x in range(N):
        sum_garo+=table[y][x]
        num_sum[y].append(sum_garo)

for _ in range(M):
    y1,x1,y2,x2 = map(int,input().split())  # 하 여기 x,y좌표 반대로 나옴
    answer = 0
    for y3 in range(y1-1,y2):       # 좌표가 1,1부터 시작하므로 각 y좌표에 -1해줘야 함
        answer+=num_sum[y3][x2]-num_sum[y3][x1-1]
    print(answer)

'''
'''
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
A = [[0]*(n+1)]
D = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    A_row = [0]+[int(x) for x in input().split()]
    A.append(A_row)

for i in range(1,n+1):
    for j in range(1,n+1):
        D[i][j]=D[i][j-1]+D[i-1][j]-D[i-1][j-1]+A[i][j]

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    print(D[x2][y2]-D[x1-1][y2]-D[x2][y1-1]+D[x1-1][y1-1])