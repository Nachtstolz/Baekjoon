# 1260 # DFS/BFS
# DFS와 BFS

# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1~N번까지 이다.

# 첫째 줄에 정점의 개수 N(1<=N<=1,000), 간선의 개수 M(1<=M<=10,000),
# 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의
# 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은
# 양방향이다. 첫째 줄에 DFS를 수행한 결과를, 다음 줄에는 BFS를 수행한 결과를 출력한다.

from collections import deque

def dfs(arr, size, visited, node) :
    visited[node] = 1
    dfs_res.append(node)
    for k in range(1, size) :
        if visited[k] == 1 : 
            continue
        if arr[node][k] == 1 :
            dfs(arr, size, visited, k)


n, m, v = map(int, input().split())
# dfs : visited, 재귀
# bfs : deque
arr = [[0] * (n+1) for _ in range(n+1)]
for i in range(m) :
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1

dfs_res = []
bfs_res = []

# dfs 구현 구간
visited_dfs = [0] * (n+1)
dfs(arr, n+1, visited_dfs, v)

# bfs 구현 구간
visited_bfs = [0] * (n+1)
q = deque()
q.append(v)
visited_bfs[v] = 1
while q:
    top = q.popleft()
    bfs_res.append(top)
    for i in range(n+1) :
        if arr[top][i] == 1 and visited_bfs[i] == 0 :
            visited_bfs[i] = 1
            q.append(i)

for i in dfs_res :
    print(i, end=' ')
print()
for i in bfs_res :
    print(i, end=' ')


