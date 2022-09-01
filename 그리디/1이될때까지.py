# N 이 K의 배수가 될 때까지 1로 뺀다.
N, K = map(int,input().split())
cnt = 0
while N != 1:       # N 이 1이 아닐 때, 계속 돌기 N이 1 이면 break
    if N%K != 0:    # N%K가 0 이 아닐 시,
        N = N-1     # N에 1 빼기
    else :
        N=N//K
    cnt += 1
print(cnt)