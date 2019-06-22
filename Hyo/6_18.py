n = int(input())

for null in range(n):

    i = input()
    i = i.split('X')
    a = i.count('')

    while True:
        i.remove('')
        a += -1
        if a == 0:break

    r = 0
    for n in i:
        b = len(n)
        i = 0
        for null in range(b):
            i += 1
            r += i

    print(r)
