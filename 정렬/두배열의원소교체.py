'''
동빈이가 가지고 있는 배열 중, A배열의 합이 최대값이 되도록 만들기
5 3
1 2 5 4 3
5 5 6 6 5
'''
N, K = map(int,input().split())
array_A = list(map(int,input().split()))
array_B = list(map(int,input().split()))
# 최대 K번 바꿔치기 가능
#바꿔주기 전, array_A와 array_B를 오름차순으로 정렬해줘야 함.
for i in range(N):
    for j in range(N-1,i,-1):
        if array_A[i]>array_A[j]:
            array_A[i],array_A[j]=array_A[j],array_A[i]
        if array_B[i] > array_B[j]:
            array_B[i], array_B[j] = array_B[j], array_B[i]


# i는 앞에서부터, j는 뒤에서부터 돌리며, 각 A의 값보다 B가 큰게 나온다면 A와 B바꿔주기
# K가 count와 같아지면 break
count = 0
for i in range(N):
    for j in range(N-1,-1,-1):
        if array_A[i]<array_B[j]:
            count+=1
            array_A[i],array_B[j]=array_B[j],array_A[i]
        if count==K:
            break
    if count==K:
        break
print(sum(array_A))
