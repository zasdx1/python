A = input()
B = input()
A1 = A.split()
B1 = B.split()
C = []
for i in range(0,int(A1[0])) :
    if int(B1[i]) < int(A1[1]) :
        C.extend(B1[i])
    

for j in range(0,len(C)) :
    D = C[j]

print(D)   


