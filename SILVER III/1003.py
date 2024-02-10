# 1003 # DP # 성공
# 피보나치 함수

# 다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.
# https://www.acmicpc.net/problem/1003 참고
# fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.
# fibonacci(3)은 fibonacci(2)와 fibonacci(1)[1]을 호출한다.
# fibonacci(2)는 fibonacci(1)[2]과 fibonacci(0)을 호출한다.
# [2]인 fibonacci(1)은 1을 출력하고 1을 리턴한다.
# fibonacci(0)은 0을 출력하고, 0을 리턴한다.
# fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고 1을 리턴한다.
# [1]인 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
# fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고 2를 리턴한다.
# 1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때,
# 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.
# 각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해 출력한다.

# n이 0, 1, 2일 경우 하드코딩
arr0 = [0] * 41
arr1 = [0] * 41
arr0[0] = 1
arr1[1] = 1
arr0[2] = 1
arr1[2] = 1

t = int(input())
while t > 0 :
    t-=1
    n = int(input())
    if n >= 3 : # DP -> 바텀업 방식 활용
        for i in range(3,n+1) :
            arr0[i] = arr0[i-1] + arr0[i-2]
            arr1[i] = arr1[i-1] + arr1[i-2]
    print(arr0[n], arr1[n])