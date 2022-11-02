# 파이프옮기기1
'''
재귀를 사용해서 경우의수를 따지면 쉬울 것 같음
대각선 방향이면 아래로 갈 수 o
오른쪽 방향이면 대각선으로 갈 수 o
'''
def dfs(a,b,a1,b1):
    global cnt
    if (a1,b1)==(N-1,N-1):
        cnt +=1
        return
    di,dj=(a1-a),(b1-b)
    if (di,dj)==(0,1):
        ni = a1
        nj = b1+1
        if 0<=ni<N and 0<=nj<N and house[ni][nj]!=1:
            dfs(a1,b1,ni,nj)
            ni+=1
            if 0<=ni<N and house[ni][nj]!=1:
                dfs(a1,b1,ni,nj)

    elif (di,dj)==(1,0):
        ni = a1+1
        nj = b1
        if 0<=ni<N and 0<=nj<N and house[ni][nj]!=1:
            dfs(a1,b1,ni,nj)
            nj +=1
            if 0<=nj<N and house[ni][nj]!=1:
                dfs(a1,b1,ni,nj)

    elif (di,dj)==(1,1):
        ni = a1+1
        nj = b1+1
        if 0<=ni<N and 0<=nj<N and house[ni][nj]!=1:
            dfs(a1,b1,ni,nj)
            nj-=1
            if 0 <= ni < N and 0 <= nj < N and house[ni][nj] != 1:
                dfs(a1, b1, ni, nj)
            nj+=1
            ni-=1
            if 0 <= ni < N and 0 <= nj < N and house[ni][nj] != 1:
                dfs(a1, b1, ni, nj)

N = int(input())
house = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
dfs(0,0,0,1)
print(cnt)




