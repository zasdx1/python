## count를 사용해 각 숫자 갯수 파악
'''
a = input()
b = input()
c = input()

mul = int(a)*int(b)*int(c)
s_mul = str(mul)

for i in range(0,10) :
    print(s_mul.count(str(i)))




#입력받은 점수를 리스트로 넣어서 40보다 작을땐 리스트값을 40으로 변경하여 평균
A = input()
B = input()
C = input()
D = input()
E = input()
EX = [A,B,C,D,E]
EXA = 0

for i in range(0,len(EX)) :
    if int(EX[i]) < 40 :
        EX[i] = 40
    EXA += int(EX[i])
#정수형 점수로
print(int(EXA/5))


#일단은 if로 풀었는데 다른 방법이 있을듯.
A = input()

if A == '1 2 3 4 5 6 7 8' :
    print('ascending')
elif A == '8 7 6 5 4 3 2 1' :
    print('descending')
else :
    print('mixed')


OX = input()
OXL = []
for j in range(0,len(OX)) :
    OXL.append(OX[j])

for i in range(0,len(OX)):
    
    if OXL[i] and OXL[i+1] == 'O' :
        OXL[i] = 1
        OXL[i+1] = 
    else :
        OXL[i] = 0

print(OXL)

'''


K = input()

L = K.split(' ')
try:
    L.remove('')
    L.remove(' ')
except:
    pass

print(len(L))

    




    




