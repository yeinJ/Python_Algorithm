food_times= [3,1,2]
k = 5 # 네트워크 장애 시간
i,a = 0,0
N = len(food_times)
while a<k :
    if food_times[i]:
        food_times[i]-=1
        i = (i+1)%(N)
        a += 1
    else :
        i = (i + 1) % (N)
print(i+1)




