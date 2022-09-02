# 볼링공 고르기
N,M = map(int,input().split()) # N 볼링공 개수 , M 최대 공의 무게
K = list(map(int,input().split()))
ans = 0
for i in range(N):          # 버블 정렬 씀 - 좋은거 없나../
    for j in range(i,N):
        if K[i] != K[j]:
            ans += 1
print(ans)
