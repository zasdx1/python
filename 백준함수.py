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

'''
#문제 1 셀프넘버 / 각자리수 0~9까지 모든경우 배열 / 최종 for문에서 나온값이 없을경우 print


N = input()


if true:
    for i in range(1,int(N)+1)
        K = str(i)
    



