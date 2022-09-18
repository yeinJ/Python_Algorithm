# 카카오 코딩테스트 60059
key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]

# 회전하기 위한 리스트 90도 회전 ( 나동빈 코드 )
def rotated(n):
    a = len(n)      # 세로
    b = len(n[0])   # 가로
    result = [[0]*a for _ in range(b)] # 회전할때는 가로 세로가 바뀜

    for i in range(a):
        for j in range(b):
            result[j][a-i-1]=n[i][j]
    return result

answer = False      # 처음 answer는 False로 설정
# M*M 배열의 key가 lock의 0부분을 모두 막아줄 수 있으면 True로 반환
# 일단 lock 값을 뽑아주기
zero_list = []
for i in range(len(lock)):
    for j in range(len(lock[0])):
        if lock[i][j]==0:
            zero_list.append([i,j])

for h in range(4): # 90도 회전은 총 4 방향으로 이루어짐
    one_list = []
    key=rotated(key)
    for i in range(len(key)):
        for j in range(len(key[0])):
            if key[i][j]==1:
                one_list.append([i,j])      # key에서는 1 값을 구해준다.
    di = [1,0,-1,0,1,-1]
    dj = [0,1,0,-1,1,-1]

    for e in range(len(one_list)):
        for k in range(6):
            cnt = 0
            ei,ej = one_list[e][0],one_list[e][1]
            g = 0
            while True :
                g += 1
                ni = ei + di[k]*g
                nj = ej + dj[k]*g
                if 0<=ni<len(lock) and 0<=nj<len(lock):
                    if [ni,nj] in zero_list:
                        cnt += 1
                        for u in range(e,len(one_list)):
                            ki,kj=one_list[u][0]+di[k]*g,one_list[u][1]+di[k]*g
                            if [ki,kj] in zero_list:
                                cnt +=1
                            else :
                                if 0<=ki<len(lock) and 0<=kj<len(lock):
                                    break
                                else :
                                    continue
                        if cnt == len(zero_list):   # one_list 변화한 값과 zero_list가 같으면 열쇠 성립
                            answer = True
                else :
                    break

                if answer == True:
                    break

            if answer == True:
                break
        if answer == True:
            break
    if answer == True :
        break

print(answer)







