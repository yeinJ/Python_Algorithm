'''
dp는 가능하면 재귀쓰면 안 됨
for문으로 해결하기!!!!!
해당 문제는 2번째줄부터 위 값 또는 왼쪽 위 값을 더해주며 진행
마지막 index에서 max 값 출력
'''
import sys
input = sys.stdin.readline
N = int(input())
pyramid = []
for _ in range(N):
    k = list(map(int,input().split()))
    pyramid.append(k)

for i in range(1,N):
    for j in range(i+1):
        if j==0:
            up_left = 0         # 왼쪽 위는 j==0일 때, 존재하지 x
        else :
            up_left = pyramid[i-1][j-1]
        if j == i :             # j == i면 존재 x 따라서 0
            up = 0
        else :
            up = pyramid[i-1][j]
        # 최대 합을 저장
        pyramid[i][j] = pyramid[i][j] + max(up_left,up)

print(max(pyramid[N-1]))

