# 0<N<=500
# N은 1이상 100,000 이하의 자연수
# 해당 데이터의 경우 데이터의 차이가 1,000,000을 넘지 않는다. 따라서 count정렬을 써보자
N = int(input())
count=[0]*100001
for _ in range(N):
    count[int(input())]+=1
for h in range(100000,0,-1):
    if count[h]:
        for i in range(count[h]):
            print(h, end=' ')
print()

