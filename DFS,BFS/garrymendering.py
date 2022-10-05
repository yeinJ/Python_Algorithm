# 17471 게리맨더링

'''
백준시를 두 선거구로 나누었을 때, 두 선거구의 인구 차이의 최솟값 출력
두 선거구로 나눌 수 없는 경우에는 -1 출력
'''
N = int(input())    # 구역의 개수
po = list(map(int,input().split()))
link=[[0]]
for i in range(N):
    Num,*arr = list(map(int,input().split()))
    link.append(arr)

