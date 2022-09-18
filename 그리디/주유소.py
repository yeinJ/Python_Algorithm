# 주유소
N = int(input())
min_price = 1000000001
road = list(map(int,input().split()))
price = list(map(int,input().split()))
ans = 0
for i in range(N-1):
    if price[i] < min_price :       # 최솟값일 시 다음 길을 갈 때 최솟값만큼 주유
        min_price = price[i]
    ans += min_price * road[i]
print(ans)

