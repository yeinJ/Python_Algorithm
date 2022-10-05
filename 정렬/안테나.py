'''
일직선상의 마을에 여러채의 집 존재
한 개의 집에 안테나 설치
- 결론 N//2 번째 집에 설치하면 됨
'''
N = int(input())
count=[0]*100001
num2 = list(map(int,input().split()))
add = []
for i in num2:
    count[i]+=1

num = []
j = min(num2)
for i in range(1,100001):       # count 정렬로 먼저 num 정렬해주기
    if count[i]>0:
        for k in range(count[i]):   # 중복된 집이 있을 수 있으니 count가 0보다 크면 count 내 값만큼 반복해서 넣어주기
            num.append(i-j) # 정렬해주면서 이전 i-1값과의 차를 add-list에 저장
            add.append(i)
        j=i

min_ans = 1e9
min_i = 0
for i in range(N):
    ans=0       # 최종 합
    ans3 =0     # 왼쪽 값의 누적 합 더하기
    for j in range(i,0,-1):
        ans3 += num[j]  # 해당 값 범위에서 누적해서 더하기
        ans+=ans3       # 누적값 계속 최종 합에 더해주기
    ans2 = 0    # 오른쪽 값의 누적 합 더하기
    for j in range(i+1,N):
        ans2+=num[j]
        ans+=ans2
    if min_ans > ans:       # 최소 구하기
        min_ans = ans
        min_i = i
print(add[min_i])

#############################


N = int(input())
num = list(map(int,input().split()))
num.sort()
if N%2:
    print(num[N//2])
else :
    print(num[N//2-1])


