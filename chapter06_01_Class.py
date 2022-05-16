# 붕어빵 처럼 찍어내는 틀로 생각하면 된다. (객체지향)
# 파이썬 클래스
# OOP(객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재

# 예제1

#진돗개 =, 리트리버 = (비효율적이며 가독성 x)
class Dog2: # object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 인스턴스가 객체에 포함된다.
# 클래스 정보
print(Dog2)

# 인스턴스화
a = Dog2("Ggomy", 2)
b = Dog2("Tanggu", 3)

# 비교
print(a == b, id(a), id(b))

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog2.species)
print(a.species)
print(b.species)

# 예제2
# self의 이해 (나만의 인스턴스 속성)
class SelfTest:
    def func1(): # 클래스 메소드로 직접 송출, 왜? : 매개 변수가 없기 때문
        print('Func1 called')
    def func2(self): # 클래스를 생성한 인스턴스화 시킨 변수 'self'로 넘어갔다.
        print(id(self))
        print('Func2 called')

f = SelfTest() # 인스턴스 변

# print(dir(f)) - func1/2
print(id(f))
# f.func1() #예외
f.func2()

SelfTest.func1()
# SelfTest.func2() #예외
SelfTest.func2(f)

# 예제3
# 클래스 변수, 인스턴스 변수

class Warehouse:
    # 클래스 변수 = 0
    stock_num = 0 #재고

    def __init__(self, name): #생성자
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self): #개체가 소멸할 때 자동으로 호출되는 함 #소멸
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee') #개체1
user2 = Warehouse('Cho') #개체2

print(Warehouse.stock_num)
# Warehouse.stock_num = 50 // 직접 접근은 나쁘다.
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', Warehouse.__dict__)
print('>>>', user1.stock_num)

del user1
print('after', Warehouse.__dict__)

# 예제4
class Dog: # object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)

# 인스턴스 생성
c = Dog('july', 4)
d = Dog('Marry', 10)
# 메소드 호출
print(c.info())
print(d.info())
# 메소드 호출
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))
