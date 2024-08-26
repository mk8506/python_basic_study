k = []
for i in range(9):
    num = int(input())
    k.append(num)
'''
max = -1
max_idx = -1
for i in range(9):
    if k[i] > max:
        max = k[i]
        max_idx = i
print(max, i+1)
'''

print(max(k))
print(k.index(max(k))+1) #약간 딕셔너리의 키처럼 인덱스