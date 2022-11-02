'''
n*m 크기의 금광
세로 (열) 부터 출발하여 금광 얻기
오른쪽 위, 오른쪽, 오른쪽 아래로 갈 수 있음
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
'''
di = [0,-1,1]
dj = [1,1,1]
T = int(input())
for tc in range(T):
    n,m = map(int,input().split())
    gold = list(map(int,input().split()))
    ma = []
    gold_memo = [[0] * m for _ in range(n)]
    for i in range(n):
        a_list = []
        for j in range(m):
            a_list.append(gold[j+(m*i)])        # 받아준 1차원 리스트값, 2차원 리스트로 바꿔주기
        ma.append(a_list)

    for i in range(n):
        gold_memo[i][0]=ma[i][0]                # 열 값을 memo 값에 저장

    j=0
    while j!=m :
        for i in range(n):
            for h in range(3):              # 오른쪽 위, 오른쪽, 아래 세 값에 memo를 해주고, 다른 i에서 시작했을때의 값과 비교
                ni=i+di[h]
                nj=j+dj[h]
                if 0<=ni<n and 0<=nj<m:
                    gold_memo[ni][nj]=max(gold_memo[ni][nj],gold_memo[i][j]+ma[ni][nj])
        j += 1

    max_gold = 0
    for j in range(n):                              # 금광의 끝 부분에서 가장 많이 캐온 값을 구한다.
        max_gold=max(max_gold,gold_memo[j][m-1])
    print(max_gold)
