# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서o, 중복o, 수정o, 삭제o)

# 선언
a = []
b = list()
c = [70, 75, 80, 85] #len
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', e[-1][1])
print('d - ', list(e[-1][1]))

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])

# 리스트 연산(생략)

# 리스트 수정, 삭제
print('>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] #[[]] 사용하면 리스트로 삽입
print('c - ', c)
del c[2] # 삭제
print('c - ', c)
print()
# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(10) # 끝에 추가
print('a - ', a)
a.sort() # 오름차순
print('a - ', a)
a.reverse() # 내림차순
print('a - ', a)
print('a - ', a.index(3), a[3])
a.insert(2, 7) # 원하는 위치에 추가
print('a - ', a)
# del a[6]
print('a - ', a)
a.remove(10)
print('a - ', a)
print('a - ', a.pop()) # 끝에 원소부터 꺼낸다.
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count("사과")) # 리스트 안에 원하는 값의 개수를 구할 때
ex = [8, 9]
a.extend(ex) # 집합체로 추가
print('a - ', a)

# 삭제 : remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)
