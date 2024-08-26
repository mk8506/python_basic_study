'''list[] need not be homogeneous, powerful tool
tup() immutable
dict{} key and value
set{} unordered
'''

'''
컬렉션 타입과 반복문
for 반복변수 in 컬렉션타입:
'''

a = [10,20,30,2,1]
for data in a:
    print(data, end=' ')
print()

for data in (10,20,30,20,10):
    print(data, end=' ')
print()

c = {'a': 10, 'b':30}
for data in c: #dic은 key를 기본으로 가져옴
    print(data, c[data])
print()


# 리스트 평균
nums = [10, 20, 30]
total = 0
for i in nums: # i = 10,20,30
    total += i
print(total/len(nums))

# another method
total = 0
for i in range(len(nums)): # i = 0,1,2
    total += nums[i]
print(total/len(nums))




# 내장 합수 sum
nums = {1, 2, 554, 54, 54, 4, 84}
print(sum(nums))



