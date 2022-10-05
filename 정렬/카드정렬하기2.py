'''
합을 더해서 해당 합을 리스트에 넣어주고 총합에서도 넣어주기
'''
import heapq1
import sys
input = sys.stdin.readline
# heapq 정렬 알고리즘 사용
N = int(input())
number=[int(input()) for _ in range(N)]
number.sort()
def card():
    ans = 0
    q = number
    while len(q)>=2:
        num = heapq1.heappop(q)      # heapq.heappop의 경우 q에서 가장 작은값부터 빼준다.
        num2 = heapq1.heappop(q)
        num3=num+num2
        ans += num3
        heapq1.heappush(q, num3)     # 총 2개의 값이 더해지므로 계속 ans에 더해주고 1개가 남으면 break 해준다.
    return ans
print(card())
