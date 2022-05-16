# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# 상대경로 : ..(부모 디렉토리), .(현재 디렉토리) -> 모듈 내부에서만 사용
# __init__.py : Python 3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추가
# 예제1
import sub.sub1.module1
import sub.sub2.module2

# 사용
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()
print()
print()

# 예제2
from sub.sub1 import module1
from sub.sub2 import module2 as m2 #alias

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

# 예제3
from sub.sub1 import * #사용하지 않는 파일도 불러들여서, 불필요한 메모리를 사용할 수 있다.
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()

module2.mod2_test1()
module2.mod2_test2()

# 예제4
from sub.sub3 import *

module3.mod3_test1()
module3.mod3_test2()
module3.mod3_test3()
module3.mod3_test4()
module3.mod3_test5()