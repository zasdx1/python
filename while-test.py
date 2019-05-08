#문제1
nnum = 0
nnum_sum = 0
while nnum <= 1000 :
    if (nnum % 3) == 0 :
        nnum_sum = nnum_sum + nnum
    nnum = nnum + 1
print(nnum_sum)

#문제 2
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
num = 0
A_sum = 0

while num < len(A) :
    if A[num] >= 50 :
        A_sum = A_sum + A[num]
    
    num = num + 1

print(A_sum)

