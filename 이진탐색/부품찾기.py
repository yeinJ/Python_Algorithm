'''
동빈이네 전자 매장에는 부품이 N개
부품은 정수 형태의 고유한 번호가 있다.
손님이 M개 종류의 부품을 대량으로 구매하겠다며 견적서 요청

'''
N = 5
M = 3
store = [8,3,7,9,2]
buyer = [5,7,9]
####
# N = int(input())
# store = list(map(int,input().split()))
# M = int(input())
# buyer = list(map(int,input().split()))
####
# store를 번호 기준으로 정렬
for i in range(N-1):
    for j in range(i,N):
        if store[i]>store[j]:
            store[i],store[j]=store[j],store[i]
# store 정렬을 count로 하기
store2 = [0]*100001         #count로 하면 O(logn)이 되므로 값이 작아진다.
for i in range(N):
    store2[store[i]]=1


# buyer
def binary_search(array,target,start,end):
    while start <= end:
        mid = (start+end)//2    # 타깃값 찾기 위한 중간값

        if array[mid]==target:
            return 'Yes'        # 타깃값이면 break
        else :
            if array[mid]>target:
                end = mid-1
            else :
                start = mid +1
    return None

for i in buyer:
    if binary_search(store,i,0,N-1)=='Yes':     # 만약 이중탐색 할 때, 값이 있다면 yes 출력
        print('yes', end=' ')
    else :
        print('no', end=' ')
print()

