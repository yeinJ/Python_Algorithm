'''
도현이의 집 N개가 수직선 위에 있음
도현이는 언제 어디서나 와이파를 즐기기 위해 공유기 C를 설치하려 함
C개의 공유기를 N개의 집에 설치
두 공유기 사이의 거리를 최대로 하는 프로그램
# start 값, end 값에 공유기를 하나씩 둔다. 그 후, mid 값에 공유기를 두기
만일 mid 값에 공유기를 두고나서 각 start - mid, end-mid 값의 사이 값 중 큰 곳에 새로 공유기를 놓는다.
'''

import sys
input = sys.stdin.readline

N,C = map(int,input().split())
home = [int(input()) for _ in range(N)]
home.sort() # 집 정렬해주기
start = home[0]
end = home[N-1]
C = C-2
ans = end-start

def binary_search(home,start,end):
    global ans,C
    while C!=0:
        mid = (start+end)//2
        for i in range(N-1):
            if home[i]<mid<home[i+1]:
                if abs(home[i]-mid) > abs(home[i+1]-mid):
                    ans=end-home[i+1]
                    C-=1
                    start = home[i+1]
                else :
                    ans = home[i]-start
                    C-=1
                    end = home[i]
            elif mid==home[i]:
                C-=1
                if home[i]-start>end-home[i]:
                    ans = home[i]-start
                else :
                    ans = end - home[i]
                end = home[i]

binary_search(home,start,end)
print(ans)
