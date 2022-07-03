# 2407 # 정답
# 조합
# nCm을 출력한다
# 조합 공식 : n! / r!(n-r)!

# 최대 입력이 클 땐 dp = dynamic programming 활용

# math 메소드 활용 가능성 인지 -> 블로그 참고하여 진행
import math
n, m = map(int, input().split())
a = math.factorial(n)
b = (math.factorial(m)) * (math.factorial(n-m))
res = a // b # // 을 써줘야. 강제 형변환은 내부에선 부동소수점이 있는 상태
print(res)

# 실패 버전
'''
n, m = map(int, input().split())

# n! 구하기
a = 1
for i in range(1, n+1) :
    print(i, n)
    a*=i
    
# r! 구하기
b = 1
for i in range(1, m+1) :
    b*=i
    
# (n-r)!
c = 1
for i in range(1, n-m+1) :
    c*=i
    
res = a/(b*c)
print(int(res))
'''
