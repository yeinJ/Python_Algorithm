# 상하좌우
L,R,U,D = (0,-1),(0,1),(-1,0),(1,0)     # L,R,U,D에 따른 방향
K = ['L','R','U','D']
F = [L,R,U,D]
N = int(input())
dir = input().split()
arr = [[0]*N for _ in range(N)]
x,y = 0,0
for i in dir :
    for k in range(4):                  # 4 방향 중 같은 값이 있다면
        if i == K[k]:
            x += F[k][0]                # 해당 값을 x,y에 더해줌
            y += F[k][1]
            if 0 <= x < N and 0 <= y < N:   # 단 범위가 0보다 크거나 같고 N보다 작아야함
                arr[x][y] += 1
            else :
                x -= F[k][0]
                y -= F[k][1]
print(x + 1, y + 1)


    # elif i == 'R':
    #     x += R[0]
    #     y += R[1]
    #     if 0 <= x < N and 0 <= y < N:
    #         arr[x][y] += 1
    #     else :
    #         x -= R[0]
    #         y -= R[1]
    # elif i == 'U':
    #     x += U[0]
    #     y += U[1]
    #     if 0 <= x < N and 0 <= y < N:
    #         arr[x][y] += 1
    #     else :
    #         x -= U[0]
    #         y -= U[1]
    # else :
    #     x += D[0]
    #     y += D[1]
    #     if 0 <= x < N and 0 <= y < N:
    #         arr[x][y] += 1
    #     else :
    #         x -= D[0]
    #         y -= D[1]
#print(arr)
