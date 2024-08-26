a = [5, 10, 15, 20, 25]
b = [10, 20, 'Hello', 'day', 'evening']
c = [20, True, ['Hello', 'day', 'me']]

# listing
print(a, type)
print(a[0], a[2])
print(a[-3])

print(b)
print(b[2])
print(b[2]+b[3], b[4])

print(c)
print(c[2][0]) # 이중리스트
print(c[2][0]+c[2][1], c[2][2])
print()

# slicing
print(a[1:4])
print(c[2][:2])
print()

d = [1, 2, 3, 4, 5]
e = [6, 7, 8]

#리스트 연산
print(d+e) # 문자열 덧셈과 같음
print(d*2) #문자열 곱셈과 같음

#리스트 길이 구하기
print(len(d))
print(len(d+e))
print()

f = [1,2,4]

'''리스트 데이터 추가, 수정, 삭제'''
# 추가
f.append(100) #맨 뒤에 추가
print(f)
f.append('first day')
print(f)

# 삽입
f.insert(2, 3) #인덱스2에 3추가, 뒤 인덱스들은 하나씩 밀림
print(f)
f.insert(-1, 'my')
print(f)
print()

# 수정
f[4] = 5 # 다시 저장해주면 됨
print(f)
f[2:5] = [4, 8, 16] # 리스트 범위 다시 저장하기
print(f)

# 삭제
del f[5]
print(f)
del f[-2]
print(f)
del f[1:3]
print(f)
print()

f.remove(8) # 직접 데이터  삭제
print(f)
f.remove(1)
print(f)

# 비어있는 리스트 만들기
k = []
b = list()
print(b)
print()

'''리스트 관련 함수들'''
nums = [10, 30, 20 ,5 ,25]
alp = ['a', 'c', 'd', 'b']

# 찾으려는 데이터의 인덱스 반환
print(nums. index(20))
print(alp.index('c'))

# 오름차순 정렬
nums.sort()
print(nums)

# 내림차순 정렬
alp.sort(reverse=True)
print(alp)

# 확장 2가지
nums += [0, -5, -10]
nums.extend(alp)
print(nums)
print()

#역순
nums.reverse()
print(nums)
print()

#데이터 비우기
nums.clear()
print(nums)





