# N개의 정수 A[1],A[2],...A[N]이 주어져 있을때, X라는 정수가 존재하는지 알아보자
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
A.sort()            # A 정렬 해주기
M = int(input())
targets = list(map(int,input().split()))
start = 0           # target값을 찾기위해 start와 end값을 A의 리스트에서 최대,최소 index로 설정
end = N-1

def binary_sort(arr,target,start,end):
    while start<=end:
        mid = (start+end)//2
        if target == arr[mid]:      # 만약 target값이 mid랑 같으면 바로 1 return
            return 1
        elif target > arr[mid]:     # 아니라면 mid보다 클 때는 start 를 mid+1로
            start = mid+1           # mid보다 작다면 end를 mid-1로 바꾸기
        else :
            end = mid-1
    return 0

for target in targets:
    print(binary_sort(A,target,start,end))
