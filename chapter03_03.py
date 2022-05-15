# 리스트
# 자료구조에서 중요
# 배열(Array) + 외부모듈로 활용

#리스트 자료형(순서o, 중복o, 수정o, 삭제 o)

#선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱 -> 원하는 데이터를 꺼내오는것
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('e - ', list(e[-1][1]))

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])

# 리스트 연산
print('>>>>>')
print('c + d', c+d)
print('c * 3', c * 3)
print("'Test' + c[0]", 'Test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:])

# Identity(id)

temp = c
print(temp, c)
print(id(c), id(temp))

# 리스트 수정, 삭제
print('>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c']
c[1] = ['a', 'b', 'c']
c[1:3] = []
del c[2] #삭제

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(10) # 리스트 마지막에 추가
print('a - +10', a)
a.sort() # 오름차 정렬
print('a - ', a)
a.reverse() # 역 정렬
print('a - ', a)
a.insert(2, 7)
print('a - ', a)
a.reverse() # 역 정렬
print('a - ', a)
a.remove(10) # 삭
print('a - ', a)
print('a - ', a.pop()) # last in first out
ex = [8, 9]
a. extend(ex) # 리스트 마지막에 추가(여러)
print(a)

# 삭제 : remove, pop, del

# 반복문 활용
while a:
    date = a.pop()
    print(date)
print("<<<<<<<<<")
