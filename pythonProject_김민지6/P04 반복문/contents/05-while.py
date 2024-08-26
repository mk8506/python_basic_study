# while문은 무한반복 / 횟수 부정

num = 1
while num<=3:
    print(num)
    num += 1  # 증감식
print()

for i in range(0,5): # 시작값, 끝값, 증감값
    print(i)
print('=')

n = 0 # 시작값
while n < 5: # 끝값
    print(n)
    n += 1 # 증감값
print()

w = 1
sum = 0
while w != 11: #조건문이 참일때만 실행되므로 거짓으로 표현해도 같음.
    sum += w
    w += 1
print(sum)
print()

a = 1
while a < 11:
    if a%2==1:
        print(a, end=' ')
    a += 1

