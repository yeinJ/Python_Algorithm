# N 명의 학생 정보, 성적에 따라 이름 출력
# 이차원배열에서 정렬할때는 lambda 사용

N = int(input())
name = [list(input().split()) for _ in range(N)]
name = sorted(name, key = lambda student:int(student[1]))
for i in range(N):
    print(name[i][0], end=' ')

