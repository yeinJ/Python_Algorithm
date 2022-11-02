'''
N 개의 도시
각 도시는 보내고자 하는 메시지가 존재
X라는 도시에서 Y라는 도시에 전보를 보내고자 한다면 X와 Y에 통로가 있어야 함
X->Y Y->X 통로 둘 다 존재해야함
C도시에서 위급상황 , C에서 보낸 메세지를 받는 도시의 개수, 도시들이 모두 메세지를 받는데 걸리는 시간 구하기
플로이드 워셜 사용
'''
n,m,c = map(int,input().split())
INF = 1e9
city = [[INF]*n for _ in range(n)]
for _ in range(m):
    x,y,z = map(int,input().split())
    city[x-1][y-1]=z

for i in range(n):
    city[i][i]=0        # 본인도시 제외

for h in range(n):
    for i in range(n):
        for j in range(n):
            city[i][j] = min(city[i][j] , city[i][h]+city[h][j])

cnt_city,time =0,0
for j in range(n):          # 만약 c도시부터 j도시들을 이동할때, INF가 아니면
    if city[c-1][j]!=INF and c-1!=j:   # C도시에서 메세지를 받을 수 있는 도시들이라는 의미
        cnt_city+=1         # city 개수 구하기
        time = max(time,city[c-1][j])    # 시간 더해주기
print(cnt_city,time)

