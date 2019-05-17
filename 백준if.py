N = input()
Z = str(0)

if int(N) <10 :
    N = Z + N
    Ns = int(Z) + int(N)
    Nss = str(Ns)
    Nn = N[1] + Nss[0]
else : 
    Ns = int(N[0]) + int(N[1])
    Nss = str(Ns)
    Nn = N[1] + Nss[0]
print(Ns)
print(Nn)