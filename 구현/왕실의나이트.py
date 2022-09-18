N = input()
start_j = ord(N[0])-97 # ord 에서 소문자 a는 97로 반환된다.
start_i = int(N[1])-1  # 0 부터 시작하도록 1을 빼준다.
knight = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]      # 말이 갈 수 있는 경우의 수
cnt=0
for i in knight:
    nj=start_j+i[1]
    ni=start_i+i[0]
    if 0<=ni<8 and 0<=nj<8:     # ni,nj는 0부터 7 사이에 존재해야 함.
        cnt += 1
print(cnt)


