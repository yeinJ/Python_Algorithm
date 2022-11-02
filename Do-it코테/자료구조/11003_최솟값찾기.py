from collections import deque
n,l = map(int,input().split())
Ai = list(map(int,input().split()))
mydeque = deque()
answer = [0]*n

for i in range(n):
    while mydeque and mydeque[-1][0]>Ai[i]:
        mydeque.pop()
    mydeque.append((Ai[i],i))

    if mydeque[0][1]<=i-l:
        mydeque.popleft()
    answer[i]=mydeque[0][0]
print(*answer)

'''
deque활용
deq_q : l범위 내에 작은 값을 담을 리스트
만일 deq_q[-1]의 값이 Ai[i]보다 크다면 deq_q.pop()
만일 deq_q[0]의 값이 Ai[i-l]값과 같다면
범위를 벗어나므로 제거하기

'''

import sys
from collections import deque

input = sys.stdin.readline
n,l = map(int,input().split())
Ai = list(map(int,input().split()))
deq_q = deque()
answer = [0]*n
for i in range(n):
    number = Ai[i]
    while deq_q and deq_q[-1]>number:   # deq 값이 존재하고 해당 값이 number보다 클 시, 제거
        deq_q.pop()
    deq_q.append(number)
    if i>=l and deq_q[0] == Ai[i-l]: # i가 l보다 크고 deq_q의 0 값이 Ai의 i-l index값과 같을시제거
        deq_q.popleft()
    answer[i]=deq_q[0]
print(*answer)


