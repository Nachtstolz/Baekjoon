# 2178 # DFS/BFS # 성공!
# 미로 탐색
# N x M 크기의 배열로 표현되는 미로가 있다.
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
# 미로가 주어졌을 때, (1,1)에서 출발하여 (N,M) 위치로 이동할 때 지나야 하는 최소의 칸 수를
# 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
# 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

# 첫째 줄에 두 정수 N,M(2<=N,M<=100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다.
# 각각의 수들은 붙어서 입력으로 주어진다.
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.


# 가는 위치마다의 칸 수 value 기록
# 0이 아닌 칸들에 대해서 value 를 graph 배열에 바로 업데이트
# min을 이용해서 최소 칸 수 업데이트

from collections import deque

def bfs(graph, visited) :
    while queue :
        top = queue.popleft() # 현재 위치
        x = top[0]
        y = top[1]
        for i in range(4) :
            tx = x + dx[i] # 동서남북 적용
            ty = y + dy[i] # 동서남북 적용
            # 구역을 벗어나지 않고, 벽에 부딪치지 않을 때
            if tx >= 0 and tx < n and ty >= 0 and ty < m and graph[tx][ty] != 0 :
                # 방문한 적 없는 위치(최솟값을 찾기 위해)
                if (tx, ty) not in visited :
                    queue.append((tx,ty))
                    visited.append((tx,ty))
                    graph[tx][ty] = graph[x][y]+1

n, m = map(int, input().split()) # n, m 입력받기
graph = [] # 저장할 미로
visited = []
for _ in range(n) : # 미로 형태 입력받기
    tmp = list(map(int, input()))
    graph.append(tmp)

x = y = 0 # 출발 지점
# 동서남북 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((x,y))
visited.append((x,y))
bfs(graph, visited)

print(graph[n-1][m-1])


