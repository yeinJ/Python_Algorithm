'''
4
1 3 1 5
'''
def what_food(i):
    global max_food
    if i>=N:
        max_food = max(max_food,sum(food))
        return
    food[i]=K[i]            # 재귀로 확인하기
    what_food(i+2)          # food(i)를 넣을때
    food[i]=0               # food에 넣지않으면 i+1로 가기
    what_food(i+1)


N = int(input())
K = list(map(int,input().split()))
food = [0]*(N+3)
max_food = 0
what_food(0)
print(max_food)

# 방법 2
# 메모이제이션
'''
개미전사 - 부족한 식량을 충당하고자 메뚜기 마을의 식량창고 공격
식량창고 - 일직선으로 이어져 있음
인접한 식량창고가 공격받으면 메뚜기 전사가 알아챔
최소 한 칸 이상 떨어진 식량창고 공격
0,1 인덱스에서 최댓값 구하기
0,1 인덱스에 저장해주기
2,3 인덱스에서 최댓값 구하기
저장해주기
4,5 인덱스에서 최댓값 구하기
저장해주기
총 합 구하기
'''
N = int(input())    # 식량창고의 개수
k = list(map(int,input().split()))
# 식량창고를 돌면서 최대값을 비교해주기
food = [0]*(N+1)
food[0]=k[0]
food[1]=k[1]
for i in range(2,N):
    food[i]=max(food[i-1],food[i-2]+k[i])
print(food[N-1])








