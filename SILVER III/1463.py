# 1463
# 1로 만들기 # 알고리즘 분류 및 코드 참고 - DP(동적 프로그래밍)

# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다.
# 3. 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
# 연산을 사용하는 횟수의 최솟값을 출력하시오.

n = int(input())

dp = [0] * (n+1)
# dp[1]은 0, 1이 1로 되는데 필요한 연산이 0회.
# dp[2]는 2가 1이 되는데 필요한 최소 연산 횟수인 1.
# 즉, dp[x]는 x가 1이 되는데 필요한 최소 연산 횟수를 저장.

# 1 / 2 / 3 진행한 경우 나누어서 진행
# Bottom-up 방식 이용
for i in range(2, n+1) :
    # 3. 1을 빼는 연산
    dp[i] = dp[i-1] + 1 # i에서 1을 빼서 i-1이 되는데 필요한 연산 = 1
    if i%2 == 0 : # 2. 2로 나누어 떨어질 때, 2로 나누는 연산
        # 1을 빼는 연산 vs 2로 나누는 연산
        dp[i] = min(dp[i], dp[i//2]+1)
    if i%3 == 0 : # 1. 3으로 나누어 떨어질 때, 3으로 나누는 연산
        # 1을 빼거나 2로 나누는 연산 vs 3으로 나누는 연산
        dp[i] = min(dp[i], dp[i//3]+1)
print(dp[n])

''' DP - TopDown 방식 풀이 ''' # 코드 서치
# 재귀 방식 이용
n = int(input())
dp = {1:0} # 딕셔너리로 초기화
# dp가 1일때 0 값을 갖는다는 의미 = 1일 때 1이 되는데 필요한 연산 횟수 0회
def rec(n) :
    if n in dp.keys() :
        return dp[n]
    if (n%3 == 0) and (n%2 == 0) : # 3, 2로 나누어 떨어지는 경우
        dp[n] = min(rec(n//3)+1, rec(n//2)+1)
    elif n%3 == 0 : # 3으로만 나누어 떨어지는 경우 vs 1을 뺀 경우
        dp[n] = min(rec(n//3)+1, rec(n-1)+1)
    elif n%2 == 0 : # 2로만 나누어 떨어지는 경우 vs 1을 뺀 경우
        dp[n] = min(rec(n//2)+1, rec(n-1)+1)
    else : # 1을 뺀 경우
        dp[n] = rec(n-1)+1
    return dp[n]

print(rec(n))


''' BFS 풀이 ''' # 코드 서치
# BFS 는 항상 최단거리를 보장.
# visited에 방문 표시와 해당 노드에 방문하는 데 걸린 횟수 함께 저장.
from collections import deque
n = int(input())
Q = deque([n])
visited = [0]*(n+1)
while Q :
    c = Q.popleft()
    if c == 1 :
        break
    if c%3 == 0 and visited[c//3] == 0 :
        Q.append(c//3)
        visited[c//3] = visited[c]+1
    if c%2 == 0 and visited[c//2] == 0 :
        Q.append(c//2)
        visited[c//2] = visited[c]+1
    if visited[c-1] == 0 :
        Q.append(c-1)
        visited[c-1] = visited[c]+1
print(visited[1])