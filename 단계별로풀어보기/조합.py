# 2407
# nCm 출력
N,M = map(int,input().split())

def comb(arr,n):
    result = []
    if n > len(arr):
        return result
    if n==1 :
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)-n+1):
            for j in comb(arr[i+1:],n-1):
                result.append([arr[i]]+j)
    return result

arr = [i for i in range(1,N+1)]
print(comb(arr,M))