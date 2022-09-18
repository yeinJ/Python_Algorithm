from heapq import heappush,nsmallest
import sys
N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    num = int(sys.stdin.readline())
    heappush(heap,num)
    K=len(heap)
    if K%2 :
        print(nsmallest(K//2+1,heap)[-1])
    else :
        print(nsmallest(K//2,heap)[-1])

# num_list = []
# for _ in range(N):
#     num_list.append(int(input()))
#     num_list.sort()
#     K=len(num_list)
#     if K%2:
#         ans=num_list[K//2]
#     else :
#         ans=min(num_list[K//2-1],num_list[K//2])
#     print(ans)
#num = [list(map(int,input().split())) for _ in range(N)]



