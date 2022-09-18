#문자열 재정렬

# K1KA5CB7
S = list(input())
N=len(S)
num, ans = 0,[]
for i in range(N):
    if S[i].isdigit():
        num += int(S[i])        # 값이 숫자면 num에 더해준다.
    else :
        ans.append(S[i])        # 값이 문자열이면 ans 에 담아준다.
ans.sort()                      # ans 문자열 정리
ans.append(num)                 # 정리된 ans에 num 넣어주기
for i in ans:
    print(i, end="")

