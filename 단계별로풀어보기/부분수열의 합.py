# 1182
'''
N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이
S가 되는 경우의 수를 구하는 프로그램을 작성

'''
import sys
input = sys.stdin.readline

N,S = map(int,input().split())
Ni = list(map(int,input().split()))
cnt = 0
for i in range(1,(1<<N)):       # 부분집합에서 공집합 제외하려면 1부터 시작
    sum_n = 0
    for j in range(0,N):
        if i&(1<<j):
            sum_n += Ni[j]
    if sum_n==S:
        cnt += 1
print(cnt)


'''

'''

# 부분수열의 합
def f(i, N):
    global answer
    global cnt
    cnt += 1
    if i == N:
        s = 0                   # 부분 집합의 합
        for i in range(N):
            if bit[i]:
                s += nums[i]
        if s == S:
            if sum(bit):
                answer += 1         # 부분집합의 합이 10인 경우의 수

    else:
        bit[i] = 1              # A[i]가 부분집합에 포함
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)

from sys import stdin
N, S = map(int, stdin.readline().split())
nums = list(map(int, input().split()))
l = len(nums)
bit = [0]*l
answer = 0
cnt = 0
f(0, l)
print(answer)
# 1, 63