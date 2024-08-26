# seperator : ㅋㅁ마 사이 출력할 데이터들을 sep='내용'
# 그니까 콤마는 자동으로 , sep=' ' default값.

print('월', '요', '일')
print('월', '요', '일', sep='')

print('2024', '04', '15', sep='-')
print('난이도: toefl', 'toeic', sep='\t>>>')
print()

# end: 문자열의 마지막을 end='내용'으로 출력

print('파이=', 3.14, end='\n') # default, 따옴표 안의 내용으로 대체되는 것!
print(1592)
print('파이=', 3.14, end='') # enter없고 붙어서 나옴
print(1592)

print(3)
print(2, end='')
print()
print(1)
print()

# sep, end 함께 사용
print(4,17, sep='+', end='=')
print(4+17)

