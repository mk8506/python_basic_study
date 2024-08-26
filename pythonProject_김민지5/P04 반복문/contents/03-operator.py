'''
복합 대입 연산자 += += *= /= %= **=
사칙연산자+대입연산자
'''

a = 100
a += 10
print(a)
# a = a + 10

a //= 10
print(a)

a **= 3
print(a)

num = 100
num += 10
num += 20
num += 30
print(num)

sum = 0
for j in range(1, 11):
    sum += j
print(sum)

# 1~10 짝수 총합
sum = 0
for k in range(1, 11):
    if k%2==0:
        sum += k
print(sum)

#  1~200 13의 배수 개수
count = 0
for i in range(1, 201):
    if i%13==0:
        count += 1
print(count)

