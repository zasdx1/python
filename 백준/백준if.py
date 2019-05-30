N = input()
Z = str(0)

for i True:
    if int(N) <10 :
        N = Z + N
        Nn = int(Z) + int(N)
        Nn = str(Nn)
        N = N[1] + Nn[0]
    else :
        Nn = int(Z) + int(N)
        Nn = str(Nn)
        N = N[1] + Nn[0]
    if int(N) == int(Nn) :
        break
        print(i)


print(i)
