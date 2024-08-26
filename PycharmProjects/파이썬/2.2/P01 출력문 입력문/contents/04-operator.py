# =대입연산자, 오른쪽의 데이터를 왼쪽 대상에 저장.

a = 10 # a에 정수 10을 대입
print(a)

b = 20
print(b)

b = a
print(b) # b에 a값을 대입하니까 b값이 바뀜
b = a + 100 # b에 대입, 100 추가
print(b)
a = b = 50 # 뒤부터 진행, 50을 b에 대입후 b값을 a에 대입
print('a =', a)
print('b =', b)

c = 'spring'
print('c =', c)
