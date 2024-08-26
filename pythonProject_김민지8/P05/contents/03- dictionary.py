# dic = {key:value}  :key중복불가, 순서없음, 변경가능

a = {'name':'nini', 'birth':'5/1', 'age':10}
b = {0:'today', 2:'is', 1:'wednesday'}
c = {1:20, 2:40, 3:60}
d = {'num1':100, 'num2':200}
e = {'pet':['dog', 'cat'], 'wild':('tiger', 'shark')}

print('dictionary a length:', len(a))
print('dictionary e length:', len(e))

print(a['name'])
print(b[2])
print(c[1])
print(d['num2'])
print(e['pet'][0])
print()

# 변경
# 추가
a['hobby'] = 'youtube'
print(a)
c[4] = 80
print(c)

# 수정
a['name'] = 'racoon'  # 추가랑 똑같음
print(a)

# 삭제
del a['hobby']
print(a)
del c[4]
print(c)
print('-'*15)
print()

# key or value 만 가져오기
print(a.keys())
print(list(a.keys()))
print(a.values())
print(list(e.values()))
print(list(a.items())) #튜플로 가져옴
print()

# key 중복
f = {'a':1, 'a':2}
print(f)

k = {'a':1, 'b':1}
print(k)

# value 찾기
print(k['a'], k.get('a')) # a의 key와 value 같이 찾기
print(k.get('c')) # none
# print(k['c']) 오류

