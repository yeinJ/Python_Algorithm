'''
n,m 주어짐
합이 m으로 나누어떨어지는 (i,j)쌍의 개수 구하기
이중for문 하면 터질거같은데..
0 1 3 6 7 9

'''
import sys
input = sys.stdin.readline
n,m = map(int,input().split()) # ex. 5개의 num_list의 연속된 값의 합 중 m으로 나눠떨어지는 수 구하기
num = list(map(int,input().split()))
num_sum = [0]
sum_i = 0
for i in num:
    sum_i+=i
    num_sum.append(sum_i)
N = 1
j = 0
answer = 0
while N<n+1:
    i = j+N
    number = num_sum[i]-num_sum[j]
    if number%m==0:
        answer+=1
    j += 1
    if i == n:
        N+=1
        j=0
print(answer)




