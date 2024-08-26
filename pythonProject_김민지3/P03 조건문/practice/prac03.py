a = int(input('정수 입력: '))
b = int(input('정수 입력: '))

print('두 수의 합은', a+b)
if a >= b: print('두 수의 차는', a-b)
else: print('두 수의 차는', b-a)

# if문 한 번만 사용
sub = a-b
if sub < 0: sub = -sub
print('두 수의 차는', sub)

