#곱하기 혹은 더하기
#왼쪽부터 오른쪽으로 더하기
#split하지 말고 받아서 for문으로 0이면 더해주고 나머지는 곱한다. but, 처음 곱할때는 ans가 0이므로 ans를 1로 바꿔준다.
num = list(map(int,input()))
ans = 0
for i in num :
    if i!=0 and i!=1 :
        if ans == 0 :
            ans=1
            ans *= i
        elif ans == 1:
            ans+=i
        else :
            ans*=i
    else :
        ans+=i
print(ans)

