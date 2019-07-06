'''
def 함수명(매개변수):
    <수행할문장1>
    <수행할문장2>
    return 결과값


def add(a, b):
    return a+b

a = 3
b = 4
c = add(a, b)
print(c)


# 입력값이 몇 개 일지 모를 때 --> *매개변수
def add_money(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_money(1,2,3,4,5)
print(result)

# 여러개의 입력을 처리할 때
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)
result = add_mul('mul', 1,2,3,4,5)
print(result)

#키워드 파라미터(Keyword arguments) : ** 매개변수명 앞에 붙이면 매개변수는 딕셔너리가 되고 모든 key=value 형태의 입력 인수가 그 딕셔너리에 저장됨

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age='3')

def add_and_mul(a, b):
    return a+b, a*b

result = add_and_mul(3, 4)
print(result)
'''


#Q1. 10000보다 작거나 같은 셀프넘버(생성자가 없는 숫자) 1줄에 1개씩 출력
# n = 1 , d(n) = 1 + 1 = 2  -> 2는 self num 아님
# n = 2 , d(n) = 2 + 2 = 2  -> 4는 self num 아님
# n = 3 , d(n) = 3 + 3 = 6  -> 6는 self num 아님
# n = 4 , d(n) = 4 + 4 = 8  -> 8는 self num 아님
# n = 5 , d(n) = 5 + 5 = 10  -> 10는 self num 아님
# n = 6 , d(n) = 6 + 6 = 12  -> 12는 self num 아님
# n = 7 , d(n) = 7 + 7 = 14  -> 14는 self num 아님
# n = 8 , d(n) = 8 + 8 = 16  -> 16는 self num 아님
# n = 9 , d(n) = 9 + 9 = 18  -> 18는 self num 아님
# n = 10 , d(n) = 10 + 1 + 0 = 11  -> 11는 self num 아님
# n = 11 , d(n) = 11 + 1 + 1 = 13  -> 13는 self num 아님
# n = 12 , d(n) = 12 + 1 + 2 = 15  -> 15는 self num 아님
# n = 13 , d(n) = 13 + 1 + 3 = 17  -> 17는 self num 아님
# n = 14 , d(n) = 14 + 1 + 4 = 19  -> 19는 self num 아님
# n = 15 , d(n) = 15 + 1 + 5 = 21  -> 21는 self num 아님
# ...
# n = 101 , d(n) = 101 + 0 + 1 = 102  -> 102는 self num 아님
# ...
# n = 1001 , d(n) = 1001 + 1 + 0 + 0 + 1 = 1004  -> 102는 self num 아님

import math

n = 101

mok = math.trunc(n/10)
nmg = n%10

selfnum = n+mok+nmg

print(n, mok, nmg, selfnum)



#자릿수체크, 나누기 10

