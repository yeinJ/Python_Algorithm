def find_processor():
    global cnt
    core = []
    for i in range(1, N - 1):
        for j in range(1, N - 1):  # 가장자리에 있는 core는 이미 연결되어 있는 core
            if processor[i][j] == 1:
                core.append((i, j))
                cnt += 1
    return core

def check(i,j):
    direction = [0, 0, 0, 0]
    for k in range(4):
        ni, nj = i, j
        length = 0
        while 0 < ni < N - 1 and 0 < nj < N - 1:
            length += 1
            ni += di[k]
            nj += dj[k]
            if processor[ni][nj]:
                break
        else:
            direction[k] = length
    return direction

def connect(i,j,d): # 선을 연결하거나 해제
    ni,nj = i,j
    while 0<ni<N-1 and 0<nj<N-1:
        ni += di[d]
        nj += dj[d]
        processor[ni][nj] ^= 1        # 선이 연결되어있으면 해제해줌, 연결안되어있으면 연결

def recur(cur,min_sum,result_cnt):
    global result
    if result_cnt > result[0]: # 연결된 개수가 더 많으면 바꿔주기
        result[0]=result_cnt
        result[1]=min_sum
    elif result_cnt == result[0]:
        if result[1]>min_sum:
            result[1]=min_sum
    if cur == cnt :      # 선 연결이 다 되면 종료
        return
    i,j = core[cur][0],core[cur][1]
    direction = check(i,j)
    for d in range(4):
        if direction[d]==0: # 만약 움직일 수 없으면 pass
            continue
        connect(i,j,d)  # 선 연결
        recur(cur+1,min_sum+direction[d],result_cnt+1)  #연결하고 다음으로
        connect(i,j,d)  # 선 해제
    recur(cur+1,min_sum,result_cnt) #연결하지 않고 다음으로

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    processor = [list(map(int,input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    cnt = 0
    core = find_processor()
    result = [0,0]  # 연결시킬 개수, 연결 길이
    recur(0,0,0)
    print(f'#{tc} {result[1]}')







