'''
N = input()
Z = str(0)

for i in :
    if int(N) <10 :
        N = Z + N
        Nn = str(Nn)
        N = N[1] + Nn[0]
    else :
        Nn = int(Z) + int(N)
        Nn = str(Nn)
        N = N[1] + Nn[0]
    
    if N == S :
        break
    

print(int(N)


N = input()
N = N.split()
x = int(N[0])
y = int(N[1])


# for문 말고 sum()을 이용해서
m_count = [31,28,31,30,31,30,31,31,30,31,30,31]
d_count = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
mon_day = 0
for j in range(0,int(x)-1) :
    if x == 1 :
        mon_day = 0
    else : 
        mon_day = mon_day + m_count[j]
total_day = mon_day + int(y)
s_s = total_day % 7
print(d_count[s_s])


'''


A = input()
S = A.split(' ')
K = []
for i in range(0,3):
    K.append(int(S[i]))

K.sort()
print(K[1])