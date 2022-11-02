
for tc in range(1,11):
    n,r = input().split()
    r=[i for i in str(r)]
    cnt = -1
    while True:
        for h in range(len(r)-1):
            cnt = 0
            if r[h]==r[h+1]:
                cnt += 1
                if h+2<=len(r)-1 and h>0:
                    r = r[:h]+r[h+2:]
                    break
                elif h==0:
                    r = r[h+2:]
                    break
                elif h+2==len(r):
                    r = r[:h]
                    break
        if cnt == 0:
            break

    print(f'#{tc} {"".join(r)}')

