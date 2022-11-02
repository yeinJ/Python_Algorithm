'''
자연수 N은 몇개의 연속된 자연수의 합으로 나타낼 수 있다.
어떤 자연수 N에 대해서 N을 몇개의 연속된 자연수의 합으로 나타낼 수 있는지
가지수 구하기
누적합으로 빼면 안될까..?
투포인터 사용
만일 sum_num이 주어진 n과 같다면 count +=1 해주고 end값 1 더해주기
더해준 end값을 sum_num에 더해준 후,
값이 커진다면 start point를 빼준 후 start점을 +=1 해준다.
start가 점차 커지면서 end와 격차를 줄여주고 최종적으로 end==n이 된 경우 while문이 멈춘다.
'''
import sys
input = sys.stdin.readline
n=int(input())

start = 1
end = 1
count = 0
sum_num = 1
while end<=n:
    if sum_num == n:
        count += 1
        end += 1
        sum_num += end
    elif sum_num > n :
        sum_num -= start
        start += 1
    else :
        end += 1
        sum_num += end

print(count)
n = int(input())
m = c = 0
while n > m:
	m += 1
	n -= m
	if n % m == 0:
		c += 1
print(c)