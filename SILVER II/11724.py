# 11724 # 그래프 이론 # DFS/BFS # 성공
# 연결 요소의 개수

# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를
# 구하는 프로그램을 작성하라. 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.
# (1 <= N <= 1,000 / 0 <= M <= Nx(N-1)/2)
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1<=u,v<=N, u=/=v)
# 같은 간선은 한 번만 주어진다.

import sys
from collections import deque
sys.setrecursionlimit(10**6) # RecursionError 해결

''' 그래프 이론 '''
def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b        

# 정점, 간선 개수
n, m = map(int, sys.stdin.readline().split())
parent = [0] * (n+1)
for i in range(1, n+1) :
    parent[i] = i
for _ in range(m) :
    u, v = map(int, sys.stdin.readline().split())
    union_parent(parent, u, v)

for i in range(1, n+1) :
    parent[i] = find_parent(parent, i)
tmp = set(parent)
print(len(tmp)-1)


''' dfs / bfs '''
def dfs(graph, visited, parent, x, child) :
    if visited[child] == 0 : # 방문하지 않은 노드일 경우
        visited[child] = 1 # 방문 처리
        parent[child] = x  # 부모 노드 기입
    else :
        return

    for i in range(1, n+1) :
        if visited[i] == 0 and graph[child][i] == 1 :
            # 방문하지 않고 연결 처리는 되어있을 때, 재귀 함수 처리
            dfs(graph, visited, parent, x, i)


def bfs(graph, visited, x) :
    q = deque([x])
    visited[x] = 1 

    while q :
        node = q.popleft()
        for i in range(1, n+1) :
            if graph[node][i] == 1 and visited[i] == 0 :
                q.append(i)
                visited[i] = 1

n, m = map(int, sys.stdin.readline().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited_1 = [0] * (n+1) # DFS용 방문 여부 확인 리스트
visited_2 = [0] * (n+1) # BFS용 방문 여부 확인 리스트
parent = [0] * (n+1) # 부모 노드 저장할 리스트

for _ in range(m) : # 연결 간선 받기
    u, v = map(int, sys.stdin.readline().split())
    graph[u][v] = graph[v][u] = 1

for i in range(1, n+1) :
    #if visited_1[i] == 0 : # 이것까지 넣으면 재귀함수 수가 줄어들 것 같음
    dfs(graph, visited_1, parent, i, i)
tmp = set(parent)
print(len(tmp)-1)

count = 0
for i in range(1, n+1) :
    if visited_2[i] == 0 :
        bfs(graph, visited_2, i)
        count+=1

print(count)



