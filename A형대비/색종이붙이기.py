def find_color(i,j):
    sum_h = 0
    no = 0
    for k in range(i,i+h):
        for e in range(j,j+h):
            if 0<=k<10 and 0<=e<10:
                if arr[k][e]==1:
                    sum_h += 1
                else :
                    no = 'imp'
                    break
        if no=='imp':
            break
    if sum_h == h**2:
        for k in range(i,i+h):
            for e in range(j,j+h):
                arr[k][e]=-1
        return h
    else :
        return 0


count = [-3]+[5]*5 # 색종이 개수

arr = [list(map(int,input().split())) for _ in range(10)]
cnt = 0
for h in range(5,0,-1):
    for i in range(10):
        for j in range(10):
            if arr[i][j]==1:
                k=find_color(i,j)
                if count[k] != -3 and count[k]!=0:
                    count[k] -= 1
                    cnt += 1
                elif count[k]==-3:
                    continue
                else :
                    if h == 2 and count[1]>4:
                        cnt+=4
                        count[1]-=4
                    else :
                        cnt=-1
                        break
        if cnt == -1:
            break


print(cnt)





