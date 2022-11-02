'''
투-포인터 사용
i는 최소 index, j는 최대 인덱스
ingred 오름차순 정렬
만일 ingred[i]+ingred[j] 가 작다면 i+=1 크다면 j-=1 해주기
m과 같다면 cnt +=1
최종적으로 cnt출력
'''
def can_make(i,j,m):
    global cnt
    while True:
        closet = ingred[i] + ingred[j]
        if closet > m:
            j -= 1
        elif closet < m:
            i += 1
        else:
            cnt+=1
            j-=1
        if i>=j:
            return

import sys
input = sys.stdin.readline
n = int(input()) # 재료의 개수
m = int(input())
ingred = list(map(int,input().split()))
ingred.sort()  # 고유 번호들 정렬
i,j = 0,n-1
cnt = 0
can_make(i,j,m)
print(cnt)


