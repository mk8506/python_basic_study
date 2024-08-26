'''
Q)  반복문을 사용하여 다음 리스트 값들 중에서
    최대값과 최소값을 찾고 평균값을 구하시오.

    ↓ 실행화면 ↓
    최대값: 85
    최소값: 3
    평균값: 42.875
'''
listK = [20, 55, 10, 3, 85, 36, 70, 64]
max = listK[0]
min = listK[0]
sum = 0
for i in range(len(listK)-1):
    if listK[i+1] > max:
        max = listK[i+1]
    if listK[i+1] < min:
        min = listK[i+1]
    sum += listK[i]
print(max)
print(min)
print(sum/len(listK))

max = listK[0]
min = listK[0]
sum = 0
for num in listK:
    if num > max:
        max = num
    if num < min:
        min = num
    sum += num
print(max)
print(min)

avg = sum/len(listK)
print(avg)
print()


result = {'최댓값':max, '최솟값':min, '평균값':avg}
for key in result:
    print(f"{key}: {result[key]}")

