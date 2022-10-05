'''
입력데이터 개수가 많은 데이터에 input을 사용하면 동작 속도가 느려
시간초과를 받을 수 있음
따라서 그럴땐 import sys 무조건
'''

import sys
input = sys.stdin.readline
N = int(input())
count = [0]*2000002     # 절대값이 1000000미만인 값들이므로 값을 받을 때, 음수를 취급하기 위해 +1000000을 더해준다,
for _ in range(N):
    num = int(input())
    count[num+1000000]=1

for i in range(2000002):    # 저장된 값을 1000000을 더해서 출력해준다.
    if count[i]:
        print(i-1000000)

