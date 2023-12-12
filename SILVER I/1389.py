# 1389 # 최단 경로 # DFS/BFS # 성공
# 케빈 베이컨의 6단계 법칙
# 케빈 베이컨의 6단계 법칙에 의하면 지구에 있는 모든 사람들은 최대 6단계 이내 서로 아는 사람으로
# 연결될 수 있다. 케빈 베이컨 게임은 임의의 두 사람이 최소 몇 단게 만에 이어질 수 있는지
# 계산하는 게임이다.
# 케빈 베이컨은 미국 헐리우드 영화배우들끼리 케빈 베이컨 게임을 했을 때 나오는 단계의 총 합이 가장 적은
# 사람이라고 한다. 오늘은 백준 온라인 저지 유저 중 케빈 베이컨 수가 가장 적은 사람을 찾으려고 한다.
# 케빈 베이컨 수는 모든 사람과 케빈 베이컨 게임을 했을 때, 나오는 단계의 합이다.
# 예를 들어, BOJ의 유저가 5명이고, 1-3, 1-4, 2-3, 3-4, 4-5가 친구인 경우를 생각해보자.
# 1은 2까지 3을 통해 2단계만에, 3까지 1단계, 4까지 1단계, 5까지 4를 통해 2단계만에 알 수 있고
# 따라서 케빈 베이컨 수는 2+1+1+2 = 6이다.
# 이런식으로 5명의 유저 중 케빈 베이컨 수가 가장 작은 사람은 3,4이다.
# BOJ 유저의 수와 친구 관계가 입력으로 주어졌을 때, 케빈 베이컨 수가 가장 작은 사람을 구하는 프로그램을 작성하시오.
# 첫째 줄에 유저 수 N(2<=N<=100)과 친구 관계의 수 M(1<=M<=5000)이 주어진다. 둘째 줄부터 M개의 줄에는
# 친구 관계가 주어진다. 친구 관계는 A와 B로 이루어져 있으며, A와 B가 친구라는 뜻이다. A와 B가 친구라면 B와 A도 친구이고
# A와 B가 같은 경우는 없다. 친구 관계는 중복되어 들어올 수도 있으며, 친구가 한 명도 없는 사람은 없다.
# 또 모든 사람은 친구 관계로 연결되어져 있다. 사람의 번호는 1부터 N까지이며, 두 사람이 같은 번호를 갖는 경우는 없다.

# 첫째 줄에 BOJ의 유저 중 케빈 베이컨의 수가 가장 작은 사람을 출력한다. 그런 사람이 여러 명일 경우
# 번호가 가장 작은 사람을 출력한다.

''' 최단 경로 - 플로이드 워셜 알고리즘 '''
'''
INF = 1e9
n, m = map(int, input().split())
arr = [[INF] * (n+1) for _ in range(n+1)] # 친구 관계 저장 배열
dist = [0] * (n+1) # 케빈 베이컨 수 저장 배열
for _ in range(m) : # 친구 관계 기록
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1

for i in range(1, n+1) :
    arr[i][i] = 0

for k in range(1, n+1) :
    for a in range(1, n+1) :
        for b in range(1, n+1) :
            arr[a][b] = min(arr[a][b], arr[a][k]+arr[k][b])

for i in range(1, n+1) :
    for j in range(1, n+1) :
        dist[i] += arr[i][j]
dist[0] = INF

print(dist.index(min(dist)))
'''

''' DFS / BFS ''' ''' 서치 참고 '''
from collections import deque
def bfs(graph, start) :
    num = [0] * (n+1) # 친구들마다의 연결 단계 저장 배열
    visited = [start] # 방문 체크
    queue = deque()
    queue.append(start)

    while queue :
        top = queue.popleft()
        for i in graph[top] :
            if i not in visited :
                visited.append(i)
                num[i] = num[top]+1
                queue.append(i)

    return sum(num)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = []
for i in range(1, n+1) :
    result.append(bfs(graph, i))

print(result.index(min(result))+1)