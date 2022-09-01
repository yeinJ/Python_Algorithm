N = int(input()) # 손님에게 거슬러줘야 할 돈
num = 0 # 동전의 최소 개수
coin = [500,100,50,10]
for i in coin:
    num+= N//i
    if N == 0 :
        break
    N=N%i
print(num)

