# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용 (탈출!!)
# I'm Boy

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)

# Raw String : 문자열 안에 특수기호를 모두 문자 그대로 표시
raw_s1 = r'D:\python\test'

print(raw_s1)

# 멀티라인 입력 (# 역슬러쉬 필수(줄바꿈 오류발생 x))
multi_str = \
"""
String
Multi line
Test
"""
print(multi_str)

# 문자열 연산 :생략
str_o1 = "Python"
str_o2 = "Apple"
str_o4 = "Amm Bmm Cmm"
# 문자열 형 변 :생략

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)
print("Capitalize ", str_o1.capitalize()) # 첫번째 시작 글자를 대문자로 수정
print("endswith? :", str_o2.endswith("e"))
print("replace", str_o1.replace("thon", 'Good')) # 해당 문자를 변경하기
print("sorted: ", sorted(str_o1)) # 정렬해서 리스트로 출력 (내림차순)
print("split: ", str_o4.split(" "))

# 반복(시퀀스)
im_str = "Good boy!"

print(dir(im_str)) # __iter__ : 반복 가능

# 출력
for i in im_str:
    print(i)

# 슬라이싱 연습
str_s1 = "Nice Python"

# 슬라이싱 연습
print(str_s1[0:3]) # 0 1 2
print(str_s1[5:]) # = [5:11]
print(str_s1[:len(str_s1)]) # 자리수를 모를 때
print(str_s1[1:4:2])

# 아스키 코드(또는 유니코드)
a = 'z'

print(ord(a)) # 아스키 코드로
print(chr(122)) # 문자로
