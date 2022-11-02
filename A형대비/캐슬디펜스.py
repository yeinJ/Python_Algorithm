'''
궁수가 공격 가능한 곳 mC3
궁수는 턴마다 적 하나 kill
적이 성으로 들어가면 게임에서 제외
모든 적이 격자판에서 제외되면 게임 끝
모든 궁수는 동시에 공격
궁수에게 가장 가까운 적이 여럿일 경우 가장 왼쪽에 있는 적 공격
같은 적이 여러 궁수에게 공격당할 수 있음
'''
N,M,D = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]+[0]*M # 궁수가 존재하는 곳을 더해주기
# monster_list = []
# for k in range(N):
#     monster = list(map(int,input().split()))
#     for h in range(M):
#         if monster[h]==1:
#             monster_list.append((k,h))

# 궁수가 있는 곳 위치 정하기
max_monster = 0
si,sj = 1,0
for i in range(M-2):
    for j in range(i,M-1):
        for h in range(j,M):        # [n,i],[n,j],[n,h] 각 궁수가 배치될 자리
            while True :










