N = int(input())
num = [int(input()) for _ in range(N)]
num.sort()
total_sum = 0
while True :
    if len(num)>1:
        a = num.pop(0)
        b = num.pop(0)
        total_sum += a + b
        num.append(a + b)
        num.sort()
    else :
        break

print(total_sum)

N = int(input())
count = [0]*int(1e9)
for i in range(N):
    count[int(input())]+=1
k=0
total_sum = 0
add_num = 0
while k!=1000000:
    k+= 1
    if count[k]==1:
        if add_num:
            add_num += k
            total_sum += add_num
            count[add_num]+=1
            add_num = 0
        else :
            add_num += k
    if count[k]>1:
        if count[k]%2:
            # count[k]는 홀수만큼 있다.
            # 이때 add가 존재한다면
            if add_num :
                add_num += k
                count[add_num]+=1
                total_sum += add_num
                add_num = 0
                count[2*k]+=(count[k]-1)//2
                total_sum += 2*k*((count[k]-1)//2)
            else :
                count[2 * k] += (count[k])// 2
                total_sum += 2*k*((count[k])//2)
                add_num += k
        else :
            if add_num :
                add_num += k
                count[add_num]+= 1
                total_sum += add_num
                add_num = k
                count[2*k]+=(count[k]-2//2)
                total_sum += 2*k*(count[k]-2//2)
            else :
                count[2*k]+=count[k]//2
                total_sum += 2*k*(count[k]//2)
print(total_sum)




# k = 1
# sum_a = 0
# total_sum = 0
# while k!=1000:
#     k+=1
#     if count[k]>1:
#         if sum_a==0:
#             sum_a+=k*count[k]
#             count[sum_a]+=1
#             sum_a = 0
#         else :
#             sum_a+=k
#             count[k]-=1
#             count[sum_a]+=1
#             total_sum += sum_a
#             sum_a = 0
#             sum_a+=k*count[k]
#             count[sum_a]+=1
#             sum_a = 0
#     elif count[k]==1:
#         if sum_a:
#             sum_a+=k
#             count[sum_a]+=1
#             total_sum += sum_a
#             sum_a = 0
#
#         else:
#             sum_a+=k
# print(total_sum)




