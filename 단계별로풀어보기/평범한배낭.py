N, K = map(int,input().split())
product=[list(map(int,input().split())) for _ in range(N)]
product.sort()
print(product)
d = [0]*(N+1)
d[0] = product[0]






