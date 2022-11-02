cnt=int(input())
count = [0]*(cnt+1)
count[1]=1
count[2]=2
i = 3
while i<=cnt:
    count[i]=count[i-2]+count[i-1]
    i+=1
print(count[cnt])




