# pop 기본개념
import sys
K = int(sys.stdin.readline())
K_list = []
for i in range(K):
    N = int(sys.stdin.readline())
    if N == 0:
        K_list.pop()
    else :
        K_list.append(N)
print(sum(K_list))


