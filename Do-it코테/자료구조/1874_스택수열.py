'''
1-n까지 수 스택에 넣었다가 뽑아 늘어놓기
하나의 수열 만들기
스택 push 순서 오름차순
1-n에서 차례대로 push 로 리스트 넣기
만일 원하는 값이 나왔다면 pop
다시 넣기
다시 넣는 과정 중, 불가능 하다면 NO 출력
'''
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
answer = deque(int(input()) for _ in range(n))
num = []
ans = []
i ,j= 1,0
while i<=n:
    if i<=answer[j]:            # 만일 i가 answer[0]보다 작거나 같다면 num리스트에 값을 넣어주고 answer리스트에 +넣어주기
        num.append(i)
        ans.append('+')
    else :                      # i가 더 크다면 목표 값을 달성하지 못하므로 (5를 빼야하는데 num[-1]은 6이고 i값이 7인 경우)
        ans = 'NO'              # ans NO로 변경하고 break
        break
    k = 0
    if i == answer[j]:
        while num:
            if num[-1]==answer[j]:      # num이 존재할 때, num마지막 인덱스와 answer[0]이 같다면
                num.pop()               # num 맨 뒤에 값 제거
                answer.popleft()        # answer는 맨 앞에 값 제거
                ans.append('-')         # 답에 - 넣기(POP하는것이므로)
                k+=1
            elif num[-1]!=answer[j] and n==i:   # num마지막 인덱스와 answer가 같지 않은데 n==i인 경우 최대값이므로 답이 안됨
                ans = 'NO'
                break
            elif num[-1]!=answer[j]:            # 그냥 값이 다른경우는 break
                break

    if ans =='NO':
        break
    i+=1

if ans=='NO':
    print(ans)
else :
    for i in ans:
        print(i)








