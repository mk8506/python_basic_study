# 중첩 반복문
for i in range(1,5):
    for j in range(1,4):
        print(f'i = {i} | j = {j}') # shift + \ = |
print('#' * 20)
print()

# 3단
for j in range(1, 10):
    print(f'{3} x {j} = {3*j}')
print('#' * 20)
print()

# 2단~9단
for i in range(2,10):
    print(f'{i}단')
    for j in range(1, 10):
        print(f'{i} x {j} = {i * j}')
    print('-'*4+'***'+'-'*4)
print('#' * 20)
print()

for i in range(2,10):
    print(f'{i}단:', end=' ')
    for j in range(1, 10):
        print(i * j, end=' ')
    print()
# 이중반복문 -> 2차원 나타내기 가능

'''
shift + 마우스스크롤 ㅋㅋㅋㅋ
shift + enter
alt + 마우스클릭 다중 선택
alt + 화살표 
alt 1,2,3,4~
'''

