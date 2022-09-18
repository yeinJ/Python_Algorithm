#1541번
ex = input()
ex_list,ineq = [],[]
ex_num = ''

for i in ex :
    if i.isdigit():                 # 값이 숫자면 ex_num문자열에 i 더해주기
        ex_num += i
    else :
        ex_list.append(int(ex_num)) # 숫자 아닐 시, ex_num 문자열에 모은 값 int값으로 변형해서 ex_list에 넣어주기
        ineq.append(i)              # 해당 i는 ineq리스트에 넣어주기
        ex_num = ''                 # ex_num 초기화

ex_list.append(int(ex_num))
plus,minus = ex_list.pop(0),0

for i in range(len(ex_list)):
    if ineq[i] == '-':              # ineq가 -일 경우
        if minus :                  # minus가 양의 값이면 plus에 넣어주고 초기화
            plus -= minus
            minus = 0
            minus += ex_list[i]
        else :                      # minus가 0일 시, minus에 값 채워주기
            minus += ex_list[i]
    else :
        if minus :                  # + 단위일 때, minus가 양수면 minus에 계속 채워주기
            minus += ex_list[i]
        else :                      # 0일 시, plus값에 계속 더해주기
            plus += ex_list[i]
print(plus-minus)









