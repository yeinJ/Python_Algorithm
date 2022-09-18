# 14719
H,W = map(int,input().split())
block=list(map(int,input().split()))
stack = []
# 빗물의 i값을 넣을 stack
volume = 0
for i in range(W):
    while stack and block[i]>block[stack[-1]]:
        top = stack.pop()
        if not len(stack):
            break
        distance = i-stack[-1]-1
        waters=min(block[i],block[stack[-1]])-block[top]
        # 가로 기준으로 최솟값에서 그보다 작은 값을 빼준다. 층대로 더하기
        volume += distance * waters
    stack.append(i)
print(volume)


