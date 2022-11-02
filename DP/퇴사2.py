"""
오늘 상담했다면, 오늘서부터 모든 가능한 모든 잡업을 진행한다.
"""
N = int(input())

memo = [0]*(N+1)                   # 가격 memo할곳
arr = [0]
for i in range(N):
    t, p = map(int, input().split())
    arr.append((t,p))               # arr에 1일부터 n일까지 기간 T와 금액 P arr에 담기

for i in range(1,N+1):              # 1부터 N+1 까지
    j = i                           # j = i
    tmp = 0
    while j < N+1:                  # j가 N+1 보다 작을 때 계속 memo에 값 업데이트 해주기
        if j <= N:
            if memo[j] <= tmp + arr[j][1]:          # j가 업데이트 할때마다 값을 올려줘야 하루 뛰고 상담했을때 돈 체크가능
                memo[j] = tmp + arr[j][1]
                tmp = memo[j]
        j += arr[i][0]
    if memo[N] < tmp:                       # 만약 tmp가 memo값보다 크다면 memo[N] 위치에 tmp로 변경해주기
        memo[N] = tmp

print(memo[N])