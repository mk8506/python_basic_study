while True:
    weight = int(input('짐의 무게는 얼마입니까? '))
    if weight >= 10:
        print('수수료는 1만원입니다')
    elif weight > 0:
        print('수수료는 없습니다')
    else:
        print('프로그램을 종료합니다')
        break
    print()

while True:
    weight = int(input('짐의 무게는 얼마입니까? '))
    if weight == 0:
        print('프로그램을 종료합니다')
        break
    elif weight >= 10:
        print('수수료는 1만원입니다')
    else:
        print('수수료는 없습니다')
    print()