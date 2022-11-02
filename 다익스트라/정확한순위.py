'''
선생님은 시험 본 학생 N명의 성적 분실하심
성적 비교한 결과의 일부만 갖고 있음
정확한 순위를 알 수 있는 학생 인원 구하기
'''
# 양쪽 값을 확인하며 플로이드 워셜 실행
n,m = map(int,input().split())
INF = 1e9
score = [[INF]*n for _ in range(n)]

for i in range(n):
    score[i][i]=0

for _ in range(m):
    a,b = map(int,input().split())
    score[a-1][b-1]=1

count=[0]*n
for h in range(n):                      # 각 양 방향을 확인하며 알고리즘 수행
    for i in range(n):
        for j in range(n):
            score[i][j]=min(score[i][j],score[i][h]+score[h][j])

for i in range(n):
    for j in range(n):                  # 만약 i,j 또는 j,i 둘 중 하나에 값이 있다면 순서를 알 수 있다는 의미
        if score[i][j] != INF or score[j][i] != INF:
            count[i]+=1                 # count[i] += 1 해주기
ans = 0
for h in range(n):
    if count[h]==n:                     # 만약 count[h]값이 n과 같다는 것은 모든 순서를 알고 있는 값이라는 의미
        ans += 1

print(ans)

