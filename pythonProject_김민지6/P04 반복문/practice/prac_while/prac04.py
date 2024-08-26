while True:
    num = int(input('숫자를 입력하시오: '))
    if num == -1:
        print('프로그램을 종료합니다.')
        break
    for i in range(num):
        print('*', end='')
    print()

