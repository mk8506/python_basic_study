# 중괄호(번호 지정 가능)  . format
print('give me {} apples.'.format('three'))

num = 5
print('there are {} grapes.'.format(num))

print('지불하실 {}은 총 {}{}입니다.'.format('금액', '$', 100))
print('내가 {0} 기린 {1}은 너가 {0} 기린 {1}보다 잘 그렸다ㅏ'
      .format('그린', '그림'))
print('my hobby is {hobby}, and I\'m {age} y/o'
      .format(age=18, hobby='photography'))

msg = 'you and {}, me and {}'.format('your cat', 'my dog')
print(msg)
print()

# f'{}'   :f문자열 포맷팅
weather = 'warm'
print(f'the weather is {weather}')

a = 10
b = 20
print(f'{a} * {b} = {a * b}')

for i in range(1, 10):
    print(f'{3} x {i} = {3 * i}')

# 소수점 둘째 자리까지
pi = 3.141592
print(f'{pi:0.2f}')

# 천단위 콤마
price = 12000
print(f'{price: ,}원')

#백분율 표현
a = 0.89374
print(f'{a:.4%}')

# %타입
# d는 정수만 들어감 소수 써도 정수부분만 들어감
print('today is %dth' %26)
print('오늘은 %d년 %d월입니다.' %(2024, 4))

#실수. 소수자리수f
print('pi = %.3f' % 3.14)

# %s 문자열
print('다음 계절은 %s입니다.' % '여름')

# %c 단일문자
print('이니셜은 %c입니다.' % 'K')