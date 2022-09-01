N,M = map(int,input().split())
max_min = 0
for _ in range(N):
    min_card = 100000
    card=map(int,input().split())
    for i in card:
        if min_card > i:
            min_card = i
   #min_card=min(card) # 가장 작은 수 찾기
    if min_card > max_min :  # 가장 작은 수 중 큰 수 찾기
        max_min = min_card
print(max_min)

'''
답안
'''
n, m = map(int,input().split())
result = 0

for i in range(n):
    data = list(map(int,input().split()))
    min_value = 10001
    for a in data :
        min_value = min(min_value,a)
    result = max(result,min_value)
print(result)
