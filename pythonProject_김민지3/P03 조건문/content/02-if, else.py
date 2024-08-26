num = 10
if num>=50:
    print('50보다 크거나 같습니다')
else: # 조건문이 거짓일때 내부 실행문 실행
    print('50보다 작습니다')

# 어떤 수가 3의 배수인지 아닌지
a = 13
if a%3 == 0:
    print('3의 배수입니다.')
else:
    print('3의 배수가 아닙니다.')

score = int(input('점수 입력: '))
if score >= 70: print('합격')
else: print('불합격')
# 실행문이 한 줄이면 한 줄로 가능


a = int(input('점수1입력: '))
b = int(input('점수2입력: '))
c = int(input('점수3입력: '))
if (a+b+c)/3 >= 80:
    k = '합격'
else:
    k = '불합격'
print('결과:', k)
