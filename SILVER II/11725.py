# 11725 # 성공 # 서치 솔루션 추가
# 트리의 부모 찾기

# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.
# 첫째 줄에 노드의 개수 N(2<=N<=100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

# 예제 1번 :
#       1
#     6   4
#   3    2  7
# 5

# def find_parent(a) :
#     return parent[a]

# def union_parent(parent, a, b) :
#     a = find_parent(a)
#     b = find_parent(b)

#     if 

''' dfs & heapq 활용 '''
# import heapq

# def dfs(q, idx) :
#     global parent
#     print(parent, q[idx])
#     dfs(q, q[idx][1])

# n = int(input())
# parent = [0] * (n+1)
# parent[1] = 1
# q = []
# for _ in range(n-1) :
#     a, b = map(int, input().split())
#     heapq.heappush(q, (a,b))
# print(q)
# dfs(q, 0)

''' bfs & 배열 활용 -> 메모리 초과 '''
'''
from collections import deque

n = int(input())
parent = [0] * (n+1)
graph = [[0] * (n+1) for _ in range(n+1)]
q = deque([])
# parent 배열 초기화
for i in range(1, len(parent)) :
    parent[i] = i

# graph에 연결된 간선 저장
for _ in range(n-1) :
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

# 1부터 찾아나가기
for i in range(len(graph[1])) :
    if graph[1][i] == 1 :
        q.append((1,i))

while q :
    # print(q)
    tmp = q.popleft()
    # print(tmp)
    parent[tmp[1]] = tmp[0]
    for i in range(2, len(graph[tmp[1]])) :
        if parent[i] == i and graph[tmp[1]][i] == 1 :
            q.append((tmp[1], i))

# print(parent)
print(*parent[2:], sep='\n')
'''

'''입력 시 값 확인 -> 배열에 저장 : 6분이나 걸려서 맞았다 '''
from collections import deque

q = deque([])
n = int(input())
parent = [0] * (n+1)

# parent 배열 초기화
for i in range(1, len(parent)) :
    parent[i] = i

graph = [0] * (n+1)
for _ in range(n-1) :
    a, b = map(int, input().split())
    if graph[a] == 0 :
        graph[a] = []
    graph[a].append(b)

    if graph[b] == 0 :
        graph[b] = []
    graph[b].append(a)
# print(graph)

for i in graph[1] :
    q.append(i)
    parent[i] = 1

while q :
    # print(q)
    edge = q.popleft()
    # print(edge)
    for i in graph[edge] :
        # print(i)
        if parent[i] == i and i != 1 :
            q.append(i)
            parent[i] = edge
    
print(*parent[2:], sep='\n')


''' (서치) 해결 풀이 확인하기 : 시간 단축 - BFS 활용 '''
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
visited = [False] * (n+1)
answer = [0] * (n+1)
graph = [[] for _ in range(n+1)] # 아예 처음부터 2차원 배열 선언

for i in range(n-1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, v, visited) :
    q = deque([v])
    visited[v] = True
    while q :
        x = q.popleft()
        for i in graph[x] :
            if not visited[i] :
                answer[i] = x
                q.append(i)
                visited[i] = True


bfs(graph, 1, visited)

for i in range(2, n+1) :
    print(answer[i])


''' (서치) 해결 풀이 확인하기 : 시간 단축 - DFS 활용 '''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
visited = [False] * (n+1)
answer = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for i in range(n-1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited) :
    visited[v]=True
    for i in graph[v] :
        if not visited[i] :
            answer[i] = v
            dfs(graph, i, visited)

dfs(graph, 1, visited)

for i in range(2, n+1) :
    print(answer[i])