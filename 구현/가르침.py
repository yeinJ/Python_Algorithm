# 백준 1062
# K개의 글자를 가르침
N, K = map(int,input().split())
# anta 와 tica 는 무조건 배워야 함. -> a n t i c 5개는 기본으로 배울 것
K1=K-5 # a n t i c 외에 배울 수 있는 단어의 수
known = ['a','n','t','i','c']
word_list = [list(input()) for _ in range(N)]
how_many= []
alphabet=[0]*26
ans = 0
if K1 < 0 :
    print(ans)
else :
    for i in word_list:
        list_alone = []
        alone=list(set(i))
        for x in alone:
            if x not in known:
                list_alone.append(x)
                alphabet[ord(x)-97] +=1
        if list_alone == []:
            ans += 1
        how_many.append(list_alone)
    print(how_many,alphabet)


