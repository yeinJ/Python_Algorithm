'''
N개의 원소를 포함하고 있음
수열이 오름차순으로 정렬되어 있음
수열에서 x가 등장하는 횟수를 계산하시오.
[1,1,2,2,2,2,3] x=2 라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력
'''
N,X= map(int,input().split())
Ni = list(map(int,input().split()))
cnt = 0
for i in range(N):
    if Ni[i]==X and Ni[i+1]!=X and i+1<N:       #Ni[i+1]에서 다른 수가 나오면 break
        cnt+=1
        break
    if Ni[i]==X:
        cnt += 1
if cnt == 0:
    print(-1)
else :
    print(cnt)

# 답지
def count_by_value(array,x):
    # 데이터 개수
    n = len(array)
    # x가 처음 등장한 인덱스 계산
    a = first(array,x,0,n-1)
    # 수열에 x가 존재하지 않는 경우
    if a == None:
        return 0 #값이 x인 원소의 개수는 0개이므로 0 반환
    # x가 마지막으로 등장한 인덱스 계산
    b = last(array,x,0,n-1)
    # 개수를 반환
    return b-a+1

def first(array,target,start,end):
    if start > end :
        return None
    mid = (start+end)//2
    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid==0 or target > array[mid-1]) and array[mid]==target:
        return mid
    # 중간점의 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif array[mid]>=target:
        return first(array,target,start,mid-1)
    # 중간점의 값 보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else :
        return first(array,target,mid+1,end)

def last(array,target,start,end):
    if start > end :
        return None
    mid = (start+end)//2
    # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if (mid==n-1 or target < array[mid+1]) and array[mid]==target:
        return mid
    # 중간점의 값 보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid]> target:
        return last(array,target,start,mid-1)
    # 중간점의 값 보다 찾고자 하는 값이 크거나 같은 경우 오른쪽 확인
    else :
        return last(array,target,mid+1,end)

n,x = map(int,input().split())
array = list(map(int,input().split()))

count = count_by_value(array,x)
# 값이 x인 원소가 존재하지 않는다면
if count == 0 :
    print(-1)
else :
    print(count)