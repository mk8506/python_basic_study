'''
타입 변환(casting) : 데이터 값도 함께 변경됨
형변환(type casting)
'''

# 정수형 <- 실수형  :실수형을 정수형으로 감싸기
num1 = int(3.14)
print(num1, type(num1))

# 실수형 <- 정수형
num2 = float(50)
print(num2, type(num2))

# 문자열 <- 실수형
msg = str(2.75)
print(msg, type(msg))

'''
# 정수형 <- 문자열   불ㄱㄴ
num0 = int('아메리카노')
print(num0)
'''

# 정수형 <- 문자열  숫자만일때, 정수가 정수로 일때 ㄱㄴ(외부 데이터 가져올 시 필요)

num3 = int('402')
print(num3, type(num3))

