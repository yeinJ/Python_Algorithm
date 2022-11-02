'''
괄호 안에는 연산자 하나
'''
def operator(ope):                          # 연산해주기 연산자 하나당 값 두개를 받아줌
    if ope[1]=='+':
        numb = int(ope[0])+int(ope[2])
    elif ope[1]=='-':
        numb = int(ope[0])-int(ope[2])
    elif ope[1]=='*':
        numb = int(ope[0])*int(ope[2])

    return list([str(numb)])                # str을 바로 list로 받으면 '11' 일 때, ['1','1']로 받아짐
                                            # 따라서 list([str(11)]) 로 받으면 ['11']로 받아집니다.

def find_num(number1,k):
    global max_num                          # 최댓값 찾기 가장 최소인 -(2**31)로 최댓값 설정해줬습니다.
    u = 0
    number = number1[:]                     # number로 number1 리스트 받은 값 재귀 돌릴때마다 계산해주기
    while len(number)>2:                    # len(number) 가 3개면 연산가능이지만 2개부터는 불가능 따라서 while문 멈춰주기
        if str(abs(int(number[u]))).isdigit():
            number = operator(number[u:u+3])+number[u+3:]       # 연산자로 계산한 값과 뒤에 남은 리스트 붙여주기
    max_num = max(max_num,int(''.join(number)))                 # number가 리스트 형태이기에 join해서 int 형태로 바꿔주기
    if k+3>len(number1):                                        # 다음으로 number1의 index가 k+3 보다 작다면 number1을 다 돌아준것이기 때문에 break
        return
    elif number1[k].isdigit():                                  # number1[k]의 음수의 경우 isdigit으로 판단 불가 따라서 int형태에서 절대값 붙여주고 다시 판단
        if k+3 == len(number):
            h = number1[:k] + operator(number1[k:k + 3])        # 만약 k+3이 len(number)와 같다는 것은 1+2 뒤에 아무것도 없다는 뜻이므로 뒤에 index 안 더해줌
        else :
            h=number1[:k]+operator(number1[k:k+3])+number1[k+3:]    # 같지 않으면 뒤에 인덱스까지 더해주기

        find_num(h,k+2)                                         # 괄호 사용했다면 재귀 돌리기
        find_num(number1,k+2)                                   # 어짜피 3개씩 묶어서 연산되기때문에 만일, 괄호를 안 사용하더라도 다음 값으로 넘어가려면 k+2 해줘야 함.


N = int(input())
max_num = -(2**31)
number1 = list(input()) # 숫자값은 항상 짝수 0,2,4
find_num(number1,0)
print(max_num)



