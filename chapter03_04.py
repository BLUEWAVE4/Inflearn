# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서o, 중복o, 수정x, 삭제x) # 불변

# 튜플의 사용은 수정과 삭제가 안된다는 특징으로, 변하면 안되는 중요한 정보에 쓰인다.

# 선언
a = () # 리스트는 []
b = (1) # 원소가 1개일때는 컴마를 사용해야 tuple 로 인식
c = (11, 12, 13, 14)
d = (100, 1000, "Ace", "Base", 'Captine')
e = (100, 1000, ('Ace', "Base", 'Captine'))

# 인덱싱
print('>>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('d - ', list(e[-1][1])) # 튜플 안에서도 list함수로 변환가능

# 수정x
#d[0] = 1500 = 에러발생

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])

# 튜플 연산
print('>>>>>')
print('c + d', c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3)) # 숫자 3의 위치가 어디인가
print('a - ', a.count(2)) # 2의 개수가 몇개인가

# 팩킹 & 언팩킹(Packing, Unpacking) ***
# 기초 수업에서 어려운 내용이지만, 정말 중요한 내용이다.

# 팩킹
t = ('foo', 'bar', 'baz', 'qux')

print(t)
print(t[0])
print(t[-1])

# 언팩킹1
(x1, x2, x3, x4) = t # 괄호가 없어도 사용가능하나, 관행상 괄호 표

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)


# 팩킹 & 언팩킹 (괄호 생량 가능)
t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)
