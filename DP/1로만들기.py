# 1로 만들기
'''
정수 x가 주어질 때, 5,3,2로 나누어 떨어지면 나눈다. or 1을 뺀다
'''
def find_min(X,cnt):
    global min_cnt
    if X==1:
        min_cnt=min(min_cnt,cnt)        # 작은 cnt 구하기
    if min_cnt <= cnt:
        return
    find_min(X-1,cnt+1)
    if X%2==0:                  # 2로 나눠떨어지면 2로 나누기
        find_min(X//2,cnt+1)
    if X%3==0:                  # 3으로 나눠떨어지면 3으로 나누기
        find_min(X//3,cnt+1)
    if X%5==0:                  # 5로 나눠떨어지면 5로 나누기
        find_min(X//5,cnt+1)

X = int(input())
min_cnt = 30001 # 정수 X가 30000이 최소이므로 -1을 30000번 한 값이 최대값이 된다. 따라서 가능한 최대값보다 min값 크게 하기
# count = [0]*30001
find_min(X,0)
print(min_cnt)

# 방법 2
# 메모이제이션
x = int(input())
count = [0]*30001
for i in range(2,x+1):
    count[i]=count[i-1]+1
    if i%2==0:
        count[i]=min(count[i],count[i//2]+1)
    if i%3==0:
        count[i]=min(count[i],count[i//3]+1)
    if i%5==0:
        count[i]=min(count[i],count[i//5]+1)
print(count[x])