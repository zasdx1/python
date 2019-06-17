#multistring.py

print("=" * 50)
print("My Program")
print("=" * 50)


# len

a = "Life is too short"
print(len(a))



#문자열(string) 대입 / 변수로 s 사용이 불가능?

string = "I eat %s apples" % "five"
print(string)


#연습문제1
pin = '881120-1068234'
print(pin.split('-'))

#연습문제2
print(pin[7])

#연습문제3
change = 'a:b:c:d'
print(change.replace(':','#'))


#연습문제4
change2 = change.split(':')
print('#'.join(change2))

##