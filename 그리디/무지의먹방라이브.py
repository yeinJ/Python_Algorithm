food_times= [3,7,2]
k = 10 # 네트워크 장애 시간

N = len(food_times)
f_min=sorted(food_times)
for i in range(N):
    if k-f_min[i]*N < 0:
        k = k - f_min[i-1]*N
        break
    else :
        #print(food_times.index(f_min[i]))
        food_times.pop(food_times.index(f_min[i]))

print(k)
print(food_times)




