# 집합 :순서없음, 중복안됨, 변경가능
a = {10, 20, 30, 20, 10}
b = {'how', 'was', 'your', 'day'}
c = set('apple')
print(a)
print(b) #일정하지 않음, 숫자는 기본 오름차순
print(c)

# 추가 or 삭제
s = {1,2 ,3}
s.add(4)
print(s)
s.update([5,6,7])
print(s)

s.remove(4)
print(s)
print()

# 교집합, 합집합, 차집합
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print('교집합:', s1 & s2)
print('합집합:', s1 | s2)
print('차집합:', s1 - s2)
print()

# 비어있는 집합
k = {} #dic으로 인식
print(k, type(k))

k = set()
print(k, type(k))
k.add(10)
print(k)




