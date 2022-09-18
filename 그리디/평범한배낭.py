N, K = map(int,input().split())
value = [list(map(int,input().split())) for _ in range(N)]
value.sort() # 작은 값부터 정렬
max_value = 0
cnt_value = 0
weight = 0
for i in range(N):
    if weight < K:
        weight += value[i][0]
        cnt_value += value[i][0]
        if cnt_value > max_value :
            max_value = cnt_value
    else :
        weight,cnt_value = 0,0
        weight += value[i][0]
        cnt_value = value[i][1]






