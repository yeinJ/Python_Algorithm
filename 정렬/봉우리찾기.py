'''
봉우리 찾기
3
1
5
5
5 3 3 5 4
10
2 1 5 2 1 7 7 2 1 5
'''

T = int(input())
for tc in range(1,T+1):
    N = int(input())+2
    height = [0]+list(map(int,input().split()))+[0]     # 봉우리 앞 뒤는 0을 붙여줌
    san = [0]
    cnt = 0
    ant = 0
    i = 0                                               # 봉우리 index 확인용 i
    while True :
        i+=1
        if i == N:                                      # 만약 i가 N이 된다면 break
            break
        if san[-1]<height[i]:                           # height[i]가 san의 마지막 index보다 크다면 봉우리로 확인
            san.append(height[i])
            for h in range(i+1,N):
                if san[-1]>height[h]:                  # height[h]가 san[-1]보다 작다면 ant += 1
                    san.append(height[h])
                    i = h
                    ant += 1
                elif san[-1]<height[h]:                 # 봉우리로 확인한 값보다 큰 값이 있으면
                    san = [height[h-1]]
                    i = h-1
                    break
            if ant > 0 :                            # ant가 0보다 크면 기준 index보다 작은 지형이 있으므로 해당 지형은 봉우리
                cnt += 1                            # cnt += 1 해줌
                ant = 0
        else :
            san.append(height[i])
    print(f'#{tc} {cnt}')




