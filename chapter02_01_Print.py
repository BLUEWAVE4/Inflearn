# 파이썬 완전 기초
# Print 사용법

print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

print()

# seprator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='') # 문자 사이 출력할 문자
print('010', '7777', '7777', sep='-')
print('python', 'google.com', sep='@')

print()

# end 옵션

print('Welcome to', end='  ') # 문자열 끝을 임의로 지정한다. 자동줄바꿈x
print('IT News', end='  ')
print('Web Site')

# file 옵션
import sys
print('Learn Python', file=sys.stdout)
print()

# format 사용(d : 정수, s : 문자열, f : 실수)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))
print()

# %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:$>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' % ('pythonstudy')) # . 절삭
print('{:10.5}'.format('pythonstudy')) # 10개중 5개만 출력

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42243))
print('{:4d}'.format(42))
print()

# %f
print('%1.8f' % (3.123145135)) #x.y / x는 정수 y는 소수
print('{:f}'.format(3.124124134))

print('%06.2f' % (3.141592653589793)) #06 총 자리수 설정
print('{:06.2f}'.format(3.141592653589793))
