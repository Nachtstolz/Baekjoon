# 1929 # 에라토스테네스의 체 # 소수 판별 원리 참고 # 정답
# 소수 구하기

# M 이상 N 이하의 소수를 모두 출력하는 프로그램을 작성하시오.
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1<=M, N<=1,000,000) M 이상 N 이하의 소수가 하나 이상
# 있는 입력만 주어진다.
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.


# 소수 확인하는 방법 : 1) 끝까지 돌면서 직접 나눠보기 2) 약수의 성질 이용해 직접 나눠보기
# 2) 약수의 성질 이용하기
#   모든 약수가 가운데 약수를 기준으로 곱셈 연산에 대해 대칭을 이룬다.
#   예를 들어, 16의 약수는 1, 2, 4, 8, 16. 이때 2x8 = 16은 8x2 = 16과 대칭.
#   따라서 우리는 특정한 자연수의 모든 약수를 찾을 때, 가운데 약수(제곱근)까지만 확인하면 된다.
#   예를 들어, 16이 2로 나누어떨어진다는 것은 8로도 나누어떨어진다는 것을 의미한다.

import math
import sys
input = sys.stdin.readline

def is_prime(x) :
    if x == 1 : # 1은 소수가 아님
        return False
    # math.sqrt(x) : 특정 숫자의 제곱근을 구하는 함수
    # x ** 2 를 통해 제곱수를 구할 수 있음 <-> x ** 0.5를 통해 제곱근을 구할 수 있음
    for i in range(2, int(math.sqrt(x))+1) :
        # 나누어 떨어지면 소수가 아님
        if x%i == 0 :
            return False
    return True

m, n = map(int, input().split())
for i in range(m, n+1) :
    if is_prime(i) :
        print(i)