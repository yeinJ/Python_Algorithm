#18185
'''
값 받는 방법
1. i 번 공장 3원
2. 연속한 두 공장 5원
3. 연속한 세 공장 7원
연속할 시, 2원씩 추가 -> 최소의 비용 만들기
3씩 끊기
'''

N = int(input())
Ai = list(map(int,input().split()))
n ,ans= 0,0
for i in range(N):
    if Ai[i] != 0:
        if n == 0 :
            ans+=Ai[i]*3
        else :
            ans+=Ai[i]*2
        n = (n+1) % 3
    else :
        n = 0
print(ans)







