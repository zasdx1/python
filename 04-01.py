#연습문제1

def is_odd(a):
    if a%2==0:
        return True
    else :
        return False

print(is_odd(5))

#연습문제2
def av(*b):
    sumb = 0
    for i in b :
        sumb += i
    return sumb/len(b)

print(av(4,5,6))