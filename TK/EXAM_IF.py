#Q1. 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

'''
score = int(input())

if score >= 0 and score <= 100 :
    if score >= 90 : print('A')
    elif score >= 80 : print('B')
    elif score >= 70 : print('C')
    elif score >= 60 : print('D')
    else : print('F')
'''

#Q2. 세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오.
# Input : 첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)
# Output : 두 번째로 큰 정수를 출력한다.
'''
N = input()
tmp = []

for i in range (0, 3):
    tmp.append(int(N.split(' ')[i]))

tmp.sort()

print(tmp[1])
'''

#Q3. 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
# 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
# 둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.

'''
N = 10
chkNum = 5

A = '1 10 4 9 2 3 8 5 7 6'
tmp = ''

for i in range (0, 9):
    if chkNum > int(A.split(' ')[i]) :
        #tmp.append(A.split(' ')[i])
        tmp += A.split(' ')[i] + ' '
print(tmp)
'''

#Q4. 세준이는 기말고사를 망쳤다.
# 세준이는 점수를 조작해서 집에 가져가기로 했다.
# 일단 세준이는 자기 점수 중에 최댓값을 골랐다.
# 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
# 예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.
# 세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

# 첫째 줄에 시험 본 과목의 개수 N이 주어진다. 이 값은 1000보다 작거나 같다.
# 둘째 줄에 세준이의 현재 성적이 주어진다. 이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.

'''
cnt = 4
score = '1 100 100 100'
score2 = ''
max = 0
sum = 0

for i in range (0, cnt) :
    if max <= float(score.split(' ')[i]):
        max = float(score.split(' ')[i])

for i in range (0, cnt) :
    t = float(score.split(' ')[i])
    t = float(t/max*100.0)
    print(t)
    score2 += str(t)+' '

for i in range (0, cnt) :
    sum = sum + float(score2.split(' ')[i])

#print(score2)
print('%0.2f' %float(sum/cnt))
'''


#Q5. 평균은 넘겠지

#Q6. 더하기 사이클
'''
N = input()

a = N[:1]
b = N[1:2]

if b == '' :
    N = a+'0'
    N = int(N)
else :
    N = a+b
    N = int(N)

cnt = 0

a = int(a)
b = int(b)
c = 0

while 1:

    if b == 0 :
       b = 10

    c = a + b

    cnt += 1

    tNum = repr(b)[-1]+repr(c)[-1]
    print('%s tNum' %tNum)

    tNum = int(tNum)

    if tNum == N :
        print('%d 사이클 일치' %cnt)
        break
    else :
        a = b
        b = c
        print('%d 사이클' %cnt)
        continue
'''