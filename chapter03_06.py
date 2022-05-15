# 집합(Set) 특징
# 집합(Set) 자료형(순서x, 중복x, 수정o, 삭제o)

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'} # 키와 밸류를 구분하지 않으면 Set 이 된다.
f = {42, 'foo', (1, 2, 3), 3.14159}

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 튜플 변환(set -> tuple)
t = tuple(b)
print(type(b), t)
print(t[0], t[1:3])
print()

# 리스트 변환(set -> list)
l = list(c)
l2 = list(e)

print(l)
print(l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6])

print('s1 & s2 : ', s1 & s2) # &은 교집합
print('s1 & s2 : ', s1.intersection(s2))

print('s1 | s2 :', s1 | s2) # |은 합집합
print('s1 | s2 :', s1.union(s2))

print('s1 - s2 :', s1 - s2) # -은 차집합
print('s1 - s2 :', s1.difference(s2))

# 중복 원소 확인
print('s1 & s2 : ', s1.isdisjoint(s2))

# 부분 집합 확인
print('subset : ', s2.issubset(s1))
print('superset : ',s1.issuperset(s2))

# 추가 & 제거
s1 = set([1, 2, 3, 4])

s1.add(5)
print('s1 - ', s1)

s1.remove(2)
print('s1 - ', s1)
#s1.remove(7)

s1.discard(7) #remove 와 동일한 기능이나 에러발생x
s1.clear()
print(s1)

a = [1, 2, 3]
a.clear()
print(a)
