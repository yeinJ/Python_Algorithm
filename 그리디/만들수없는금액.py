#만들 수 없는 금액
N = int(input())
coin = list(map(int,input().split()))
coin.sort() # 오름차순 정렬해주기
coin_sum= []
if coin.count(1) == 0:
    ans = 1
else :
    num = set([i for i in range(2,1000001)])
    for i in range(1<<N):
        sum_coin = 0
        for j in range(N):
            if i & (1<<j):
                sum_coin+=coin[j] # 집합 만들기
        if sum_coin in num :      # 집합의 합이 만들어진 num 안에 있으면 제거해주기
            num.remove(sum_coin)
    ans = min(num)                # 제거되지 않은 값 중 가장 작은 값 출력

    #     coin_sum.append(sum_coin)
    # num = set([i for i in range(1,1000001)]) #자연수는 1000000이하의 자연수
    # ans=min(num-set(coin_sum)) #coin_sum과 num의 차집합을 구한 후, 차집한 중 가장 작은 수 출력

print(ans)
'''
풀이 
'''
n = int(input())
data = list(map(int,input().split()))
data.sort()
target = 1
for x in data :
    if target < x:
        break
    target += x
print(target)


