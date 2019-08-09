'''
Q1. 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
입력 : 첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.
출력 : 첫째 줄부터 N번째 줄 까지 차례대로 출력한다.
'''

'''
n = 3

if n <= 100000 :
    for i in range(1, n+1):
        print(i)
'''


'''
Q2. 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
입력 : 첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.
출력 : 첫째 줄부터 N번째 줄 까지 차례대로 출력한다.
'''

'''
n = 3

if n <= 100000 :
    for i in range(n, 0, -1):
        print(i)

'''

'''
Q3. N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.
입력 : 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.
출력 : 출력형식과 같게 N*1부터 N*9까지 출력한다.
'''

'''
n = 3 #int(input())

if n >= 1 and n <= 9:
    for i in range(1, 10):
        print ('%d * %d = %d' % (n, i, n*i))
'''

'''
Q4. 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
입력 : 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
출력 : 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
'''

'''
n = 3

if n >= 1 and n <= 100 :
    for i in range(0, n):
        print('*' * (i+1))
'''


'''
Q5. 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.
입력 : 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
출력 : 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
'''


#1 = [1-4] , 5
#2 = [1-3] , 4-5
#3 = [1-2] , 3-5
#4 = [1-1] , 2-5
#5 = [0-0] , 1-5

'''
n = int(input())

if n >= 1 and n <= 100 :
    for i in range(1, n+1):
        print(" " * (n-i) + "*" * i)
'''

'''
Q6. 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제
입력 : 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
출력 : 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

in = 5 

out
*****
****
***
**
*
'''

# 1 = 5
# 2 = 4,
# 3 = 3
# 4 = 2
# 5 = 1

'''

n = int(input())

if n >= 1 and n <= 100 :

    for i in range(1, n+1):
        print('*' * (n+1-i))

'''

'''
Q7. 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제
하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

입력 : 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
출력 : 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.


in = 5

out

*****
 ****
  ***
   **
    *
'''

# 1 = '*' * 5, ' ' * 0
# 2 = '*' * 4, ' ' * 1
# 3 = '*' * 3, ' ' * 2
# 4 = '*' * 2, ' ' * 3
# 5 = '*' * 1, ' ' * 4


'''

n = 5 #int(input())

if n >= 1 and n <= 100 :

    for i in range(1, n+1):
        print(' '*(i-1) + '*'*(n+1-i))

'''

'''
Q8. 오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.

입력 : 첫째 줄에 빈 칸을 사이에 두고 x(1≤x≤12)와 y(1≤y≤31)이 주어진다. 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.

출력 : 첫째 줄에 x월 y일이 무슨 요일인지에 따라 SUN, MON, TUE, WED, THU, FRI, SAT중 하나를 출력한다.
'''

'''
# 1월 1일 = MON
# 3월 14일 = WED

n = input()
x = int(n.split(" ")[0])
y = int(n.split(" ")[1])


month_1 = [1, 3, 5, 7, 8, 10, 12] #31일
month_2 = [4, 6, 9, 11] #30일

week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']


if x >= 1 and x <= 12 and y >= 1 and y <= 31:

    for i in range(1, x+1):

        for j in range(1, )
'''