# 문자형 중요

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용
# I'm Boy

print('I\'m boy')
print()

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
print()

# 탭, 줄 바꿈
t_s1 = "Click \t start!"
t_s2 = "New Line \nCheck!"

print(t_s1)
print(t_s2)

# Raw String (운영체제 경로 설정이나 표시에 유용)
raw_s1 = r'D:\python\test'

print(raw_s1)
print()

# 멀티라인 입력
# 역슬러시 사용
multi_str = \
"""
String
Multi line
Test
"""
print(multi_str)

# 문자열 연산

# 문자열 함수(upper, isalnum, stratswith, count, endswith, isalpha...)



# 슬라이싱
str_s1 = "Nice Python"

# 슬라이싱 연습
print(str_s1[0:3]) # 3-1 -> 0 1 2
print(str_s1[5:11])
print(str_s1[:len(str_s1)])
print(str_s1[::-1])

# 아스키 코드(또는 유니코드)
a = 'z'

print(ord(a))
print(chr(122))
