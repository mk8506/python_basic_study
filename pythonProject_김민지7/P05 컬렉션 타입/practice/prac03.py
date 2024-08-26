'''
k = list()
count = 0
total = 0
for i in range(1, 101):
    if i%3==0 and i%2!=0:
        k.append(i)
        count += 1
        total += i
print(k)
print('average:', total/count)
'''

k = list()
total = 0
for i in range(1, 101):
    if i%3==0 and i%2!=0:
        k.append(i)
        total += i
print(k)
print('average:', total/len(k))