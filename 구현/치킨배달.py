# 15686
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
house,store,ans = [],[],0
for i in range(N):
    for j in range(N):
        if arr[i][j]==1:
            house.append([i,j])
        if arr[i][j]==2:
            store.append([i,j])

store_list = []
for i in house:
    min_road = 9999999999999999999999
    for j in store :
        road = abs(i[0]-j[0])+abs(i[1]-j[1])
        if road < min_road :
            min_road = road
            if j not in store_list:
                store_list.append(j)
    ans += min_road
print(ans)




