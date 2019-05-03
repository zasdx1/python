##딕셔너리 자료

dic = {'name':'pey', 'phone':'010000000', 'birth':'1188'}
print(dic['name'])

#key 객체 만들기
print(dic.keys())

#key 리스트 만들기
print(list(dic.keys()))

#key, value 쌍 얻기
print(dic.items())

#연습문제1
sample_dic = {'name':'홍길동','birth':'1128','age':'30'}
print(sample_dic.keys())

#연습문제3 - C라는 key가없을때 70 리턴
a = {'A':90, 'B':80}
print(a.get('C','70'))