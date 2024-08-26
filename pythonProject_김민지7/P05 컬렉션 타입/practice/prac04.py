# linear searching
k = [10,9,8,7,6,5,4,3,2,1]
n = int((input('찾을 데이터: ')))
for i in range(len(k)):
    if k[i]==n:
        print('{}번째 데이터입니다.'. format(i+1))
        break

print(f'{k.index(n)+1}번째 데이터입니다.')

