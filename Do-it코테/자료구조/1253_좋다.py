'''
투-포인터 사용
Ai 정렬
a = 0
b = 마지막 인덱스
i와 a또는 b값이 같다면 a인덱스는 +=1 b는 -=1 해주기
그 외에는 합을 구해서 Ai[i]값과 비교
Ai[i]보다 크면 b값 줄이고, 작으면 a값 늘림
같다면 True 리턴해주고 good += 1해주기
'''
n = int(input())
Ai = list(map(int,input().split()))
Ai.sort()
good = 0
for i in range(n):
    # i는 현재 목표 값
    a,b = 0,n-1
    ans = False
    while True:
        if i==a:
            a+=1
        elif i==b:
            b-=1
        else :
            k=Ai[a]+Ai[b]
            if a>=b :
                break
            if k>Ai[i]:
                b-=1
            elif k<Ai[i] :
                a+=1
            else :
                ans = True
                break

    if ans==True:
        good +=1
print(good)

