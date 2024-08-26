count = 0
while True:
    ans = input('문자를 입력하시오: ')
    if ans == 'a':
        count += 1
    if ans == '.':
        break
print('문자 a의 개수는', count)

