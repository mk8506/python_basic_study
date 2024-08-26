start = int(input('first number: '))
stop = int(input('last number: '))
count = 0
for i in range(start, stop+1):
    if i%4==0:
        count += i
print(f'{start}부터 {stop}까지의 4의 배수들의 합은 {count}')