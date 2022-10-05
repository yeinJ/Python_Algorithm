from itertools import combinations
import sys

N,K = map(int,sys.stdin.readline().split())
# a-z 26개
# 기본으로 배울 단어
base = ['a','n','t','i','c']
rest = ['']*N
K = K-5
if K < 0 :
    ans = 0
elif K == 21:
    ans = N
else :
    all_word = []
    for i in range(N):
        word = sys.stdin.readline().rstrip()[4:-4]
        for j in set(word):
            if j not in base:
                rest[i]+=j
                all_word.append(j)
    learn = combinations(set(all_word), K)
    max_word = 0
    for i in learn:
        word_cnt = 0
        for h in range(N):
            cnt = 0
            for j in range(K):
                if i[j] in rest[h]:
                    cnt += 1  # 만약 해당 단어가 rest내에 있으면 단어 개수 세기
            if cnt == len(rest[h]):  # 해당하는 단어가 rest단어의 개수와 같으면 word 를 배운 것이다.
                word_cnt += 1  # 배운 단어 개수 추가
        max_word = max(max_word, word_cnt)
    ans = max_word
print(ans)





