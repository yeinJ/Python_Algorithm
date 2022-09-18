k=list('abcdefghijklmnopqrstuvwxyz')
T = int(input())
for tc in range(1,T+1):
    alphabet=list(input())
    N = len(alphabet)
    cnt = 0
    for i in range(N):
        if alphabet[i] == k[i]:
            cnt += 1
        else :
            break
    print(f'{tc} {cnt}')
