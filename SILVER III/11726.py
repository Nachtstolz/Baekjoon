# 11726 # DP # Top-down으로 풀이 # Bottom-up 추가
# 추후 배열에 값 저장 -> 활용하는 방식 찾아보기
# 2xn 타일링

# 2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
# 아래 그림은 2x5 크기의 직사각형을 채운 한 가지 방법의 예이다. -> 페이지 그림 참고

# 첫째 줄에 n이 주어진다(1<=n<=1000)
# 첫째 줄에 2xn 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

# 2 -> 2
# 3 -> 3
# 4 -> 5
# 5 -> 8
# 가로 형태의 1x2의 개수를 늘려가며 해보는 방식
# n/2개의 가로형태뭉치를 놓을 수 있음
n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 2

def func(n) :
    if dp[n] > 0 :
        return dp[n]
    dp[n] = func(n-1) + func(n-2)

    return dp[n]

print(func(n)%10007)

''' 인터넷 참고 코드 1 ''' # Bottom up
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 2
for i in range(3, n+1) :
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])