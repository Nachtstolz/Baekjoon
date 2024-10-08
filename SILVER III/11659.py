# 11659 # 성공
# 구간 합 구하기 4

# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

# 첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은
# 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.
# 총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.
# 1 <= N <= 100,000
# 1 <= M <= 100,000
# 1 <= i <= j <= N

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr[0]
# dp 통해서 0인덱스 ~ 현 인덱스까지 합 구하기
for i in range(1,n) :
    dp[i] = dp[i-1]+arr[i]

#print(dp)
for k in range(m) :
    i, j = map(int, input().split())
    # 0~j까지의 합 - 0~i까지의 합
    if i < 2 :
        print(dp[j-1])
    else :
        print(dp[j-1] - dp[i-2])