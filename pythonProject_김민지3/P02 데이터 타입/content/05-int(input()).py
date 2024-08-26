# 정수/실수로 데이터 입력받기
numA = input('입력: ')
print('numA:', numA, type(numA))
# input은 기본적으로 str으로 저장.

numB = int(input('정수 입력: '))
print('numB:', numB, type(numB))
# 저장받을 변수를 타입변환하고 싶다면 input을 둘러싸기

numC = float(input('실수 입력: '))
print('numC:', numC, type(numC))
# 정수 입력하라는데 실수 불가능, 반대로는 가능

