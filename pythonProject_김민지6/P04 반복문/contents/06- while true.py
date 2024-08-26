# 조건식을 참으로 시작 -> 무한반복 -> break으로 빠져나오기(if문과 함께) exit

# 1~5까지 출력
a = 1
while True:
    print(a)
    if a == 5:
        break
    a += 1
# if문의 위치에 따라 달라짐

b = 1
while True:
    if b%2 ==0:
        print(b, end= ' ')
    if b == 20:
        break
    b += 1
print()

while True:
    print('반복을 멈추려면 Q를 입력하시오')
    c = input('입력: ')
    if c == 'Q':
        break

while True:
    print('반복을 멈추려면 -1을 입력하시오')
    c = int(input('입력: '))
    if c == -1:
        print('프로그램을 종료합니다')
        break

# continue 다음 반복의 반복문 처음으로 돌아감 continue 다음 줄 실행문 스킵
k = 0
while k < 20:
    k += 1
    if k%5==0:
        continue
    print(k, end=' ')
print()