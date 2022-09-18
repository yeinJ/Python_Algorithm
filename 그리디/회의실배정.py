#회의실배정
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
arr=sorted(arr)                 #회의실 값 앞에서부터 정렬
min_time = arr[0]
cnt = 1
for i in range(1,N):            # 끝나는시간<=시작시간일 시 , min_time 교체
    if min_time[1] <= arr[i][0]:
        min_time = arr[i]
        cnt += 1
    elif min_time[0]<=arr[i][0] and min_time[1]>=arr[i][1]:     # 1의시작시간<=2의시작시간, 1의끝나는시간>=2의끝나는시간
        min_time = arr[i]
print(cnt)

# for i in range(N):
#     cnt = 1
#     for j in range(i+1,N):
#         if arr[i][1] <= arr[j][0]:
#             cnt += 1
#             arr[i] = arr[j]
#     if cnt > max_cnt :
#         max_cnt = cnt