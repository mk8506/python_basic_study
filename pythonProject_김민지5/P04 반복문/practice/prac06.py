num = int(input('팩토리얼 입력: '))
fac = 1
for i in range(num, 0, -1):
    fac *= i
print(f'{num}! = {fac:0.0f}')