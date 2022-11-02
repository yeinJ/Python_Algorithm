# 16637
'''
수식은 왼쪽에서부터 순서대로
수식에 괄호를 추가하면 괄호 안에 들어있는 식은 먼저 계산
괄호 안에는 연산자 하나만 들어있어야 함
괄호를 적절히 추가해 만들 수 있는 식의 결과 최댓값을 구하는 프로그램 만들기
괄호에 제한은 x, 추가하지 않아도 됨
정답은 2^31보다 작고 -2^31보다 큼
정수는 0<=x<=9
'''

N = int(input())
nums = input()
N1 = N//2
num_list =[]        # 숫자값 넣을 list
ope_list =[]        # 연산자 넣을 list
number = 0
for num in nums:
    if num.isdigit():
        num_list.append(int(num))
    else :
        ope_list.append(num)
max_num = -(2**31)
numb = [0]*N
if len(num_list)%2!=0:
    numb[0]=num_list[0]
    i=2
    while i <= N1:
        if ope_list[i - 2] == '*':
            numb[i - 1] = numb[i - 2] * num_list[i - 1]
            if ope_list[i - 1] == '+':
                numb[i - 1] = max(numb[i - 1] + num_list[i], numb[i - 2] * (num_list[i - 1] + num_list[i]))
            elif ope_list[i - 1] == '-':
                numb[i - 1] = max(numb[i - 1] - num_list[i], numb[i - 2] * (num_list[i - 1] - num_list[i]))
            else:
                numb[i - 1] = max(numb[i - 1] * num_list[i], numb[i - 2] * (num_list[i - 1] * num_list[i]))
        elif ope_list[i - 2] == '-':
            numb[i - 1] = numb[i - 2] - num_list[i - 1]
            if ope_list[i - 1] == '+':
                numb[i - 1] = max(numb[i - 1] + num_list[i], numb[i - 2] - (num_list[i - 1] + num_list[i]))
            elif ope_list[i - 1] == '-':
                numb[i - 1] = max(numb[i - 1] - num_list[i], numb[i - 2] - (num_list[i - 1] - num_list[i]))
            else:
                numb[i - 1] = max(numb[i - 1] * num_list[i], numb[i - 2] - (num_list[i - 1] * num_list[i]))
        else:
            numb[i - 1] = numb[i - 2] + num_list[i - 1]
            if ope_list[i - 1] == '+':
                numb[i - 1] = max(numb[i - 1] + num_list[i], numb[i - 2] + (num_list[i - 1] + num_list[i]))
            elif ope_list[i - 1] == '-':
                numb[i - 1] = max(numb[i - 1] - num_list[i], numb[i - 2] + (num_list[i - 1] - num_list[i]))
            else:
                numb[i - 1] = max(numb[i - 1] * num_list[i], numb[i - 2] + (num_list[i - 1] * num_list[i]))
        numb[i] = max(numb[i - 1], numb[i])
        i = i + 2
    print(numb[N // 2])
    print(numb)

else :
    numb[0]=num_list[0]-num_list[1]
    i=5
    while i<=N1 :
        if ope_list[i-2]=='*':
            numb[i-1]=numb[i-2]*num_list[i-1]
            if ope_list[i-1]=='+':
                numb[i-1]=max(numb[i-1]+num_list[i],numb[i-2]*(num_list[i-1]+num_list[i]))
            elif ope_list[i-1]=='-':
                numb[i-1] = max(numb[i-1]-num_list[i],numb[i-2]*(num_list[i-1]-num_list[i]))
            else :
                numb[i-1] = max(numb[i-1]*num_list[i],numb[i-2]*(num_list[i-1]*num_list[i]))
        elif ope_list[i-2]=='-':
            numb[i-1]=numb[i-2]-num_list[i-1]
            if ope_list[i-1]=='+':
                numb[i-1]=max(numb[i-1]+num_list[i],numb[i-2]-(num_list[i-1]+num_list[i]))
            elif ope_list[i-1]=='-':
                numb[i-1] = max(numb[i-1]-num_list[i],numb[i-2]-(num_list[i-1]-num_list[i]))
            else :
                numb[i-1] = max(numb[i-1]*num_list[i], numb[i-2]-(num_list[i-1]*num_list[i]))
        else :
            numb[i-1]=numb[i-2]+num_list[i-1]
            if ope_list[i-1]=='+':
                numb[i-1]=max(numb[i-1]+num_list[i],numb[i-2]+(num_list[i-1]+num_list[i]))
            elif ope_list[i-1]=='-':
                numb[i-1] = max(numb[i-1]-num_list[i],numb[i-2]+(num_list[i-1]-num_list[i]))
            else :
                numb[i-1] = max(numb[i-1]*num_list[i],numb[i-2]+(num_list[i-1]*num_list[i]))
        numb[i]=max(numb[i-1],numb[i])
        i=i+2
    max_number = numb[N//2]
    numb = [0] * N
    max_num = -(2**31)
    numb[0]=num_list[0]
    i=2
    while i <= N1:
        if ope_list[i - 2] == '*':
            numb[i - 1] = numb[i - 2] * num_list[i - 1]
            if ope_list[i - 1] == '+':
                numb[i - 1] = max(numb[i - 1] + num_list[i], numb[i - 2] * (num_list[i - 1] + num_list[i]))
            elif ope_list[i - 1] == '-':
                numb[i - 1] = max(numb[i - 1] - num_list[i], numb[i - 2] * (num_list[i - 1] - num_list[i]))
            else:
                numb[i - 1] = max(numb[i - 1] * num_list[i], numb[i - 2] * (num_list[i - 1] * num_list[i]))
        elif ope_list[i - 2] == '-':
            numb[i - 1] = numb[i - 2] - num_list[i - 1]
            if ope_list[i - 1] == '+':
                numb[i - 1] = max(numb[i - 1] + num_list[i], numb[i - 2] - (num_list[i - 1] + num_list[i]))
            elif ope_list[i - 1] == '-':
                numb[i - 1] = max(numb[i - 1] - num_list[i], numb[i - 2] - (num_list[i - 1] - num_list[i]))
            else:
                numb[i - 1] = max(numb[i - 1] * num_list[i], numb[i - 2] - (num_list[i - 1] * num_list[i]))
        else:
            numb[i - 1] = numb[i - 2] + num_list[i - 1]
            if ope_list[i - 1] == '+':
                numb[i - 1] = max(numb[i - 1] + num_list[i], numb[i - 2] + (num_list[i - 1] + num_list[i]))
            elif ope_list[i - 1] == '-':
                numb[i - 1] = max(numb[i - 1] - num_list[i], numb[i - 2] + (num_list[i - 1] - num_list[i]))
            else:
                numb[i - 1] = max(numb[i - 1] * num_list[i], numb[i - 2] + (num_list[i - 1] * num_list[i]))
        numb[i] = max(numb[i - 1], numb[i])
        i = i + 2

    if ope_list[-1]=='*':
        numb[N//2-1]*=num_list[-1]
    elif ope_list[-1]=='-':
        numb[N//2-1]-=num_list[-1]
    else:
        numb[N//2-1]+=num_list[-1]
    if numb[N//2-1]>max_number:
        max_number=numb[N//2-1]
    print(numb)
    print(max_number)











