'''
연속하면 한꺼번에 뒤집을 수 있음
연속 x 시 한꺼번에 뒤집을 수 없다.
001100 일 시 -> 11만 뒤집어서 000000으로 만들 수 있음
그러나 010101 이면 3번 뒤집어야 함.
'''
# 0 과 1 이 분리될 때의 값이 작은것을 ans로 함
S = list(map(int,input()))

cnt_0 = 0
cnt_1 = 0
if S[0]:
    cnt_1 += 1  # 첫번째 index가 1 일 경우
else:
    cnt_0 += 1  # 첫번째 index가 0일 경우

for i in range(len(S)):
    if i-1>=0:
        if S[i]==1 and S[i-1]==0:
            cnt_1 += 1
        if S[i]==0 and S[i-1]==1:
            cnt_0 += 1
if cnt_1 > cnt_0 :
    ans = cnt_0
else :
    ans = cnt_1
print(ans)

S = list(map(int,input()))

zero_cnt = 0
one_cnt = 0
for i in range(len(S)-1):
    if S[i] == 0 and S[i] != S[i+1]:    # 0일때 다음이 1이면 0그룹 +1
        zero_cnt += 1
        if i == len(S)-2:               # 마지막 2개가 다른경우
            one_cnt += 1

    if S[i] == 1 and S[i] != S[i+1]:    # 1일때 다음이 0이면 1그룹 +1
        one_cnt += 1
        if i == len(S)-2:               # 마지막 2개가 다른경우
            zero_cnt += 1
print(zero_cnt,one_cnt)
print(min([zero_cnt, one_cnt]))