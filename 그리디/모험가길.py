# 모험가 길드
# 공포도가 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있음
# max 잘 활용하기
N = int(input())
member = list(map(int,input().split()))
arr = [[] for _ in range(N)]
# member 정렬하기 방법 1
for i in range(N):
    for j in range(i,N):
        if member[i] > member[j]:
            member[i],member[j] = member[j],member[i]
# member 정렬하기 방법 2
member=sorted(member)
num,lenum = 1,1

while num<N : # member가 0보다 클 때 정렬한 member에서의 최댓값부터 차례로 찾아준다.
    for i in range(member[-lenum]):
        arr[lenum].append(member[-num])
        num += 1
    lenum += 1

lit = 0
for i in range(N):
    if arr[i] and (len(arr[i])==max(arr[i])):
        lit+= 1

print(lit)

'''
해설
'''
n = int(input())
data = list(map(int,input().split()))
data.sort()
result = 0
count = 0
for i in data :
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)