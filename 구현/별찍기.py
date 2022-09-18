# 별찍기
N = int(input())
cnt = 1
for i in range(1,2*N,2):
    print(' '*(N-cnt) +'*'*i)        # 별의 앞부분은 별이 증가할때마다 1씩 감소
    cnt += 1