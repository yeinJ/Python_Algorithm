jump = list(map(int,input().split()))
'''
2칸 ,3칸 index가 0이 아니라면 *2 칸 까지 점프 가능
'''
n = len(jump)
count = [0]*n
count[0]=jump[0]
count[1]=jump[0]
for i in range(0,n):
    if i==0:
        count[i]=max(jump[i+2],jump[i+3])
    else :
        count[i]=max(jump[i+2],jump[i+3],jump[i*2])
    for j in range(0,i):
        count[j]=count[i]
print(count)

