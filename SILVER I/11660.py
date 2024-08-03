# 11660 # DP # 누적 합 # 인터넷에서 알고리즘 적용 방법 참고 # 성공
# 구간 합 구하기 5

# NxN개의 수가 NxN 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오.
# (x,y)는 x행, y열을 의미한다. 예를 들어, N=4이고 표가 아래와 같이 채워져 있는 경우를 살펴보자
# 1 2 3 4
# 2 3 4 5
# 3 4 5 6
# 4 5 6 7
# 여기서 (2,2)부터 (3,4)까지 합을 구하면 3+4+5+4+5+6 = 27이고, (4,4)부터 (4,4)까지 합을 구하면 7이다.
# 표에 채워져 있는 수의 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.

# 첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다. (1<=N<=1024, 1<=M<=100,000)
# 둘째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다. 다음 M개의 줄에는 네 개의 정수
# x1, y1, x2, y2가 주어지며 (x1, y1)부터 (x2, y2)의 합을 구해 출력해야 한다.
# 표에 채워져 있는 수는 1000보다 작거나 같은 자연수이다. (x1 <= x2, y1 <= y2)

''' 인터넷 검색 결과 찾은 핵심 '''
# (1, 1)에서 (x2, y2)까지의 누적 합에서 해당되지 않는 부분을 빼주면 된다.
# ⭐️ 아이패드에 그린 그림 참고하기 ⭐️
# 즉, dp 테이블의 누적 합을 구할 때 각 요소를 일일이 하나씩 더해주는 것이 아닌, 보텀업 방식으로 dp 테이블 구성.
# 이전에 계산되었던 누적 합들을 그대로 가져오면서 동작.

''' 단순 계산 -> 시간 초과 '''
'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for i in range(n) :
    arr.append(list(map(int, input().split())))

answer = []
for i in range(m) :
    res = 0
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1-1, x2) :
        for y in range(y1-1, y2) :
            res+=arr[x][y]
    answer.append(res)
for i in answer :
    print(i)
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
dp = [[0] * (n+1) for _ in range(n+1)]
for i in range(n) :
    arr.append(list(map(int, input().split())))

# 누적합 계산 -> dp 저장. 보텀업 방식 사용
for i in range(1, n+1) :
    for j in range(1, n+1) :
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1] # arr은 0부터 등록되기에
# print(dp)

# 원하는 구간 계산
for i in range(m) :
    x1, y1, x2, y2 = map(int, input().split())
    res = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(res)
