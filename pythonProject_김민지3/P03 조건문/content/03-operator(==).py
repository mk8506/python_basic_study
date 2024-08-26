'''
# 관계연산자 (비교연산자)  >, <, >=, <=, ==, !=
참 또는 거짓으로 제공
'''
a = 10 > 5
print(a, type(a))

# == 서로 같은가(같으면 true, 다르면 false), != 서로 다른가(다르면true, 같으면 false)
c = 10 == 10
print(c)
d = 'rat' == 'Rat'
print(d)
e = 10 != 11
print('e =', e)
f = 'Dog' != 'Dog'
print('f =', f)

# 관계연산자는 동시에 여러 개 사용 가능
print(50>30>20)
print(50>40==20)

