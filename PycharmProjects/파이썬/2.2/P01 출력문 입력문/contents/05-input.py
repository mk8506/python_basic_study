# 입력문: input()

print('입력하시오: ', end='')
a = input() # a에 실행칸에 쓴 내용 대입됨
a = input('입력하시오: ') # 위 두줄과 동일. 괄호안 내용 뒤에 실행칸에 쓴 내용 들어감
print(a)

Weather = input('how\'s the weather today ')
print('today\'s weather is', Weather)
print()

# 2번 입력 받고 출력
ID = input('creat id: ')
PW = input('creat password: ')
print(ID, ', your password is', PW, '.')