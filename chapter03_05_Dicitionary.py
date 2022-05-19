# 파이썬 딕셔너리
# 범용적으로 가장 많이사용
# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

# 선언 (Key : value)
a = {'name': 'Kim', 'phone': '01033337777', 'birth': '940506'}
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'Niceman',
    'City': 'Seoul',
    'Age': 33,
    'Grade': 'A',
    'Status': True
}
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade', 'A'),
    ('Status', True)
])

# 쉽고 가독성 좋음
f = dict(
    Name='Niceman',
    City='Seoul',
    Age=33,
    Grade='A',
    Status=True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 출력
print('a - ', a['name']) # 존재x -> 에러
print('a - ', a.get('name')) # 존재x - None 에러
print()
print('f - ', f.get('City'))

# 딕셔너리 추가
a['address'] = 'seoul'
print(a)
a['rank'] = [1, 2, 3]
print(a)

# dict_key, dict_values, dict_iteams : 반복문(__iter__))에서 사용 가능
print('a - ',a.keys())
print('b - ',b.keys())
print('c - ',c.keys())
print('d - ',d.keys())

print('a - ',list(a.keys()))
print('b - ',list(b.keys()))

print('a - ',a.values())
print('b - ',b.values())
print('c - ',c.values())
print('d - ',d.values())

print('a - ',list(a.values()))
print('b - ',list(b.values()))

print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())

print('a - ', list(a.items()))
print('b - ', list(b.items()))
print()

print('a - ', a.pop('name'))
print('a - ', a)
print()

print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)

# 수정
print('a - ', 'birth' in a)
a['test'] = 'test_dict'

a['address'] = 'dj'
print('a - ', a)

a.update(birth='910904')
print('a - ', a)

temp = {'address': 'Busan'}
a.update(temp)
print(temp)
