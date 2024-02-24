# 2579 # DP # 성공 -> 풀이 방식 약간 서치
# 계단 오르기

# 계단 오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임이다.
# 각각의 계단에는 일정한 점수가 쓰여 있는데 계단을 밟으면 그 계단에 쓰여있는 점수를 얻게 된다.
# 계단 오르는 데는 다음과 같은 규칙이 있다.
# 1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다다음 계단으로
# 오를 수 있다.
# 2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 3. 마지막 도착 계단은 반드시 밟아야 한다.
# 따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 하지만, 첫 번째 계단을 밟고
# 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.
# 각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하라.

# 입력의 첫째 줄에 계단의 개수가 주어진다.
# 둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다.
# 계단의 개수는 300 이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000 이하의 자연수이다.
'''
n = int(input())
arr = []
dp = [0] * n
for i in range(n) :
    arr.append(int(input()))

dp[n-1] = arr[n-1]
# 탑다운 방식으로
if n == 1 :
    print(dp[n-1])
    exit(0)

# n >= 2
for i in range(n-2, -1, -1) :
    print(i)
    print(dp)
    if i == n-2 : 
        dp[n-2] = arr[n-1] + arr[n-2]
    elif i == n-3 :
        dp[n-3] = arr[n-1] + arr[n-3]
    else :
        # 만약 dp[i+1]이 dp[i+2]+arr[i+1]이면
        # dp[i] = max(dp[i+2], arr[i+1]+dp[i+3]) + arr[i]
        
        #dp[i+4]+arr[i+2]+arr[i+1]
        if dp[i+1] == dp[i+2]+arr[i+1] :
            dp[i] = max(dp[i+2], arr[i+1]+dp[i+3]) + arr[i]
        else :
            dp[i] = max(dp[i+1], dp[i+2]) + arr[i]
        print('dp[{0}] : {1}'.format(i, dp[i]))
print(dp)
print(max(dp[0], dp[1]))
'''
# 10
# 100 100 1 1 100 100 1 1000 1000 1000 에서 오류 발생
# 100 100 1 1 100 100 1 1000 1000 1000
#              1   1  0   1    0    1
#           1  0   1  1   0   1     1

# 바텀업 방식으로 재진행 -> 풀이 찾아본 후
n = int(input())
stairs = []
dp = [0] * n
for i in range(n) :
    stairs.append(int(input()))

if n >= 1 :
    dp[0] = stairs[0]
if n >= 2 : 
    dp[1] = stairs[0]+stairs[1]
if n >= 3 :
    dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])
    for i in range(3, n) :
        dp[i] = max(dp[i-3]+stairs[i-1], dp[i-2]) +stairs[i]
print(dp[n-1])