# 연습문제1
for num in range(100) :
    num = num + 1
    print(num)

# 연습문제2
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
print(A[0])
aveA = 0
i = 0
for i in range(len(A)) :
    i = i + 1
    aveA = aveA + A[i]

print(aveA/len(A))

# 연습문제3
numbers = [1, 2, 3, 4, 5]

result = [n*2 for n in numbers if n%2==1]

print(result)

