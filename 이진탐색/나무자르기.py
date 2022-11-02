'''
높이를 H로 지정했을 때, 상근이가 가져갈 수 있는 길이가 M과 같을 때를 찾는다.
parametric search 문제
시작점 0 끝점 가장 긴 나무의 길이
H는 시작점과 끝점의 절반으로 설정

'''
N, M = map(int,input().split())
height = list(map(int,input().split()))
start = 0
end = max(height)
result = 0
while start <= end :
    target = (start+end)//2     # target값은 나무 길이의 최댓값과 가장 최소인 0으로 설정
    total = 0                   # 적어도 M의 길이를 가져가기 위해서 M보다 클 경우 total에 계속 저장
    for x in height :
        if x > target :
            total += x-target       # 만약 target보다 작은 값이면 저장할 필요 x
    if total < M :
        end = target-1
    else :
        if target ==M :     # target에 도달했다면 while문 종료
            result = target
            break
        result = target
        start = target + 1
print(result)

