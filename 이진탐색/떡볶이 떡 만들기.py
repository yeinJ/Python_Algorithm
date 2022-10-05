'''
동빈이네 떡의 길이는 일정하지 x
떡의 총 길이는 절단기로 잘라서 맞춰줌
떡의 길이를 기준으로 이진탐색하기
만일 떡의 길이가 mid 값보다 크다면? -> 시작값을 mid값 +1 로 바꿔주기
작다면 -> 끝값을 mid값 -1로 바꿔주기
해당 변화를 토대로 떡의 길이 M에 도달하는 mid 값을 찾는다.
'''
N,M = map(int,input().split())
dduck = list(map(int,input().split()))
# 떡 정렬
dduck.sort()
def binary_sort(arr,target,start,end):
    while start <= end:
        mid = (start+end)//2
        buy_dduck = 0
        for i in range(N):
            if arr[i]>mid:
                buy_dduck += arr[i]-mid     # 만약 mid값보다 떡길이가 길면 잘라서 더하기
        if buy_dduck==target:               # target값에 도달하면 return
            return mid
        else:
            if buy_dduck < target:
                end = mid-1
            else :
                start = mid +1
print(binary_sort(dduck,M,0,max(dduck)))
