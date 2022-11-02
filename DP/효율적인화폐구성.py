'''
N가지 종류의 화폐
화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 함

'''
n,m = map(int,input().split())
check = [1e9]*(10001)
k_list = []
for i in range(n):
    k = int(input())    # 각 화폐 가치들은 1로 표기
    check[k]=1          # k값에 해당하는 부분은 1
    k_list.append(k)
for i in range(m+1):    # m 까지 메모이제이션
    for k in k_list:    # k리스트에 존재하는 값들을 i값에서 빼줄 때, 해당 값이 1e9가 아닌 다른값이 있다면 min 값 바꿔주기
        if 0<=i-k and check[i-k]:
            check[i]=min(check[i],check[i-k]+1)

if check[m]==1e9:
    print(-1)
else :
    print(check[m])
