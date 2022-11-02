'''
민호 생물좋아하네..
A C G T 문자열 길이
'''

s,p =map(int,input().split())
cnt = 0
dna=list(input())
need_dna=list(map(int,input().split()))
need = ['A','C','G','T']
needs = dict(zip(need,need_dna))
# p는 사용할 문자열의 길이
for i in range(s-p+1):
    need_i=needs.copy()      # 필요한 개수 복사
    s_dna=dna[i:i+p]    # 자른 리스트
    for j in s_dna:
        if need_i[j]!=0:
            need_i[j]-=1
    if set(need_i.values())=={0}:
        cnt += 1
    else :
        continue
print(cnt)





