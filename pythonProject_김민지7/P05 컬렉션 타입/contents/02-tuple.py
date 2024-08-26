# 튜플 :데이터 변경 불가능, 소괄호 사용

a = (5, 10, 15, 20, 25)
b = (10, 20, 'Hello', 'day', 'evening')
c = (20, True, ('Hello', 'day', 'me'))

print(a, type, len(a))
print(a[1], a[-2])
print(b[2] + b[-2])
print(c[0] + c[1])
print(c[2])
print()

print(a[2:])
print(b[0:5:2])  # [시작값:끝값:스텝]
print(b[::2])
print(c[2][::2])
print()

d = [1, 2, 3, 4, 5]
e = [6, 7, 8]
# 튜플 연산
f = d + e
print(f)
k = e * 3
print(k)

# 인덱스 찾기
print(k.index(7))  # linear search
print(k.index(7, 2))  # 7값을 인덱스2부터 탐색
# 뒤에서부터 음수로 세는 건 사람만...

# 튜플값을 리스트로 변환
a = (1, 2, 3)
p = list(a)
print(p, type(p))
