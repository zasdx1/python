#문제3 / N숫자에서 1뺀만큼 한줄에 표시 / N은 총 행의 수

#문제2 / 99까지는 무조건 등차수열
'''
N = input()
K = 0

for i in range(100,int(N)+1):
    j = str(i)
    if (int(j[1])-int(j[0])) == (int(j[2])-int(j[1])):
        K += 1


max_K = K + 99

if int(N) <100 :
    print(N)
else : 
    print(max_K)


#문제 1 자리수에 따라 리스트로 구분하여 더하기

D1 = []
D2 = []
D3 = []
D4 = []


for i in range(1,10000):
    K = str(i)

    if i<10:
        F = 2*i
        D1.append(F)
        
    elif i<100:
        F = i + int(K[0])+int(K[1])
        D2.append(F)
    elif i<1000:
        F = i + int(K[0])+int(K[1])+int(K[2])
        D3.append(F)
    else :
        F = i + int(K[0])+int(K[1])+int(K[2])+int(K[3])
        D4.append(F)

pre_D_sum = D1+D2+D3+D4
D_sum = sorted(set(pre_D_sum))

for j in range(1,10000):

    if j in D_sum:
        pass
    else:
        print(j)

'''


#1행 23 * 23
#2행 22 * 1 * 22
#3행 21 


A = "{0:^10}".format("hi")
print(A)