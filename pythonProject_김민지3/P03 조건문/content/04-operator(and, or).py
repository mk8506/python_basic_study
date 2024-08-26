# 논리연산자 and, or , not

a=50
b=30
c=10
print(a>30 and b>20) # 둘 다 참일 때만 참
print(a>30 and b>30) # false 하나 있음 -> false
print(a>30 or b>30) # 하나라도 참이면 참
print(a>60 or b>30) # 모두 거짓이여서 거짓

print(not a>30)
print(not a>b>c)
print()

math = 90
science = 75
if math>= 90 and science>=80:
    print('합격')
else:
    print('불합격')

music = 70
art =70
if music>=80 or art>=80:
    print('pass')
else:
    print('retest')

