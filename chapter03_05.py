# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서x, 키 중복x(사전에서 중복된 내용 무의미), 수정 o, 삭제o)

# 선언
a = {'name': 'Kim', 'phone': '01033337777', 'birth': '940506'} #딕셔너리는 {}
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'SeonGwan',
    'City': 'Damyang',
    'Age': 29,
    'Grade': 'A',
    'Status': True
}
e = dict([
    ('Name', 'SeonGwan'),
    ('City', 'Damyang'),
    ('Age', 29,),
    ('Grade', 'A'),
    ('Status', True)
])
f = dict(
    Name='SeonGwan',
    City='Damyang',
    Age=29,
    Grade='A',
    Status=True
)

# 상당히 효율적인 자료구조

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()

# 출력
print('a - ', a['name']) # 키가 없을경우 에러발생
print('a - ', a.get('name')) # 키가 없을경우 "None" 출력
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))

# 딕셔너리 추가
a['address'] = 'seoul'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

# 딕셔너리 추가
print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))

# dict_key, dict_values, dict_items : 반복문(__iter__)에서 사용 가능

print('a - ', a.keys())
print('a - ', list(a.keys()))
print('a - ', a.values())
print()

print('a - ', a.items())
print('>>>>>>')

print('a - ', a.pop('name'))
print('a - ', a)
print()

print('f - ', f.popitem()) # 추첨기 만들때 사용
print(f)
print('f - ', f.popitem())
print(f)
print('f - ', f.popitem())
print(f)
print('f - ', f.popitem())
print(f)

print()

print('a - ', 'birth' in a)
print('a - ', 'City' in a)

# 수정 & 추가
a['test'] = 'test_dict' #수정 1
print('a - ', a)

a['address'] = 'dj'
print('a - ', a)

a.update(birth='910101') #수정 2(가독성)
print('a- ', a)
temp = {'address': 'Busan'}

a.update(temp)
print('a - ', a)
