'''
수열의 각 원소Ai에 대한 오큰수 구하기
Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중 가장 왼쪽에 있는 수
오른쪽 값에서 앞에 값보다 큰 값 ans리스트에 인덱스와 넣기

'''
import sys
input = sys.stdin.readline
n = int(input())
Ai = list(map(int,input().split()))
NGE =[0]*(n-1)+[-1]
for i in range(n-1):
    for j in range(i+1,n):
        if Ai[j]>Ai[i]:
            NGE[i]=Ai[j]
            break
    if NGE[i]==0:
        NGE[i]=-1
print(*NGE)
# '''
# '''
import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
Ai = list(map(int,input().split()))
NGE =[0]*(n-1)+[-1]
max_ans = deque()
for i in range(n):
    max_ans.append((Ai[i],i))

for i in range(n-1):
    k = 0
    while max_ans and i>=max_ans[0][1]:
        max_ans.popleft()
    if max_ans:
        while True:
            if max_ans[k][0] <= Ai[i]:
                k += 1
            else :
                NGE[i]=max_ans[k][0]
                break
            if k==len(max_ans):
                NGE[i]=-1
                break
    else :
        NGE[i]=-1


print(*NGE)





