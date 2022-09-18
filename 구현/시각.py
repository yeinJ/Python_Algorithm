# 시각
N = int(input())
ans = 0
for i in range(N+1):            # 시,분,초의 경우를 세주기
    for j in range(60):
        for h in range(60):
            if '3' in str(i)+str(j)+str(h):
                ans += 1
print(ans)