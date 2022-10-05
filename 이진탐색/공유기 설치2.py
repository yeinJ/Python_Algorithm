def binary_search(array,target,start,end):
    global C,line
    while start <= end :
        mid = (start+end)//2
        if array[mid]==target:
            C-=1
            line=min(target-start,end-target)
            if C == 0:
                break
        elif array[mid]>target :
            end = mid-1
        else :
            start = mid +1
    return None

import sys
input = sys.stdin.readline
N,C = map(int,input().split())
house = [int(input()) for _ in range(N)]
C = C-2
house.sort()
line =0
while C>0 :
    binary_search(house,house[N//2],house[0],house[-1])
print(line)
