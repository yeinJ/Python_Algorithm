N,M,K = map(int,input().split())
Ni=list(map(int,input().split()))
Ni=sorted(Ni)#정렬하기
big = Ni[-1] # 최댓값
big_2=Ni[-2] # 최댓값 바로 전 값
ans=big*M-(big-big_2)*(M//K) # 최댓값 을 M만큼 더하고 M//K의 몫 만큼 (최댓값-최댓값다음값)의 차를 빼줌
print(ans)

'''
답안
'''

n,m,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0
while True :
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m-=1
print(result)