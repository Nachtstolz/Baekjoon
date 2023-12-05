# 11724 # 그래프 이론 # DFS/BFS 적용 방법 추후 예정 - 231206 00:24
# 연결 요소의 개수

# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를
# 구하는 프로그램을 작성하라. 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.
# (1 <= N <= 1,000 / 0 <= M <= Nx(N-1)/2)
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1<=u,v<=N, u=/=v)
# 같은 간선은 한 번만 주어진다.

import sys

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