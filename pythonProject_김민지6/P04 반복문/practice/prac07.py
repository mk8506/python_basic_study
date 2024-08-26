# 삼각형 모양으로 * 출력하기!
for i in range(1, 6):
    print('*'*i)

#이차원으로 생각하기! 이중중첩문
for i in range(1,6):
    for j in range(1,i+1):
        print('*', end='')
    print()

for i in range(4, -1, -1):
    for j in range(1, i+1):
        print(' ', end='')
    for k in range(1, 6-i):
        print('*', end='')
    print()

# i번째줄: 빈칸 (5-i)개, 별표 i개
for i in range(1, 6):
    for j in range(5-i):
        print(' ', end='')
    for k in range(i):
        print('*', end='')
    print()

#크리스마스 트리 별찍기
for i in range(1, 6):