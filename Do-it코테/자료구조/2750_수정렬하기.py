
# 책에서는 merge sort로 푸는게 좋다함
N = int(input())
num = [int(input()) for _ in range(N)]
# num 리스트도 받고, sort해주기
num.sort()
for i in num:
    print(i)    