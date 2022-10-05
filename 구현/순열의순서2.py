import sys
input = sys.stdin.readline

def f(i,k,a):
    global arr,cnt
    if i == k :
        cnt += 1
        if a == 1:
            if cnt == arr[0]:
                print(*p)
        else :
            if p == arr:
                print(cnt)
    else :
        for j in range(k):
            if used[j]==0:
                used[j]=1
                p[i] = ai[j]
                f(i+1,k,a)
                used[j]=0


N = int(input())
a,*arr = map(int,input().split())
ai = [i for i in range(1,N+1)]
cnt = 0
used =[0]*N
p = [0]*N
f(0,N,a)




