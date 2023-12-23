# 2583 # DFS / BFS # 서치 참고 # 성공! # 231223 01:15 DFS 코드 짜보기
# 영역 구하기

# 눈금의 간격이 1인 MxN(M,N<=100)크기의 모눈종이가 있다. 이 모눈종이 위 눈금에 맞추어
# K개의 직사각형을 그릴 때, 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로
# 나뉘어진다. 예를 들어, M=5 N=7인 모눈종이 위 <그림1>같이 직사각형 3개를 그리면 나머지 영역은
# <그림2>같이 3개의 분리된 영역으로 나뉘어진다. 그 넓이는 각각 1, 7, 13이다.
# M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때 K개의 직사각형 내부를 제외한 나머지 부분이
# 몇 개의 분리된 영역으로 나누어지는지, 그리고 분리된 각 영역 넓이가 얼마인지 구하여 출력하는 프로그램을 작성하라.

# 첫째 줄에 M, N, K가 빈칸을 사이에 두고 차례로 주어진다. M, N, K는 모두 100 이하 자연수이다.
# 둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형 왼쪽 아래 꼭짓점의 x,y 좌표값과 오른쪽 위 꼭짓점의 x,y 좌표값이
# 빈칸을 사이에 두고 차례로 주어진다. 모눈종이 왼쪽 아래 꼭짓점의 좌표는 (0,0) 오른쪽 위 꼭짓점의 좌표는 (N,M)
# 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.

# 첫째 줄에 분리되어 나누어지는 영역 개수를 출력한다. 둘째 줄에는 각 영역의 넓이를 오름차순 정렬해 빈칸을 사이에 두어 출력.

# 주어진 직사각형 영역은 1 처리
# 0으로 남아있는 영역들에 대해 상하좌우 이동하면서 갈 곳 있는지 체크 & 넓이 동시 계산 -> 막혔으면 그만!
# bfs 처리 가보자고

from collections import deque
import sys
sys.setrecursionlimit(10**6)

def dfs(x, y) :
    global size
    if (x < 0 or x >= m) or (y < 0 or y >= n) :
        return 0
    if graph[x][y] == 1 :
        return 0
    
    graph[x][y] = 1
    size+=1
    for k in range(4) :
        dfs(x+dx[k], y+dy[k])

    return size
    
def bfs(x, y) :
    queue = deque()
    queue.append((x,y))
    size = 1
    while queue :
        top = queue.popleft()
        x = top[0]
        y = top[1]
        for i in range(4) :
            tx = x + dx[i]
            ty = y + dy[i]
            if (0 <= tx < m) and (0 <= ty < n) and graph[tx][ty] == 0 :
                graph[tx][ty] = 1 # 방문 표시를 기존 graph에 동시에
                queue.append((tx, ty))
                size += 1
    return size

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
res = []
for _ in range(k) :
    x1, y1, x2, y2 = map(int, input().split())
    
    # (2,0) (4,4) -> (2,0) (3,3) -> (1,0) (2,3) (좌측 상단 기준)
    # (1,1) (5,2) -> (1,1) (4,1) -> (0,1) (3,1) (좌측 상단 기준)
    # (0,4) (2,6) -> (0,4) (1,5) -> (3,4) (4,5) (좌측 상단 기준)
    for i in range(x1, x2) :
        for j in range(y1, y2) :
            graph[j][i] = 1 # 벽인 부분을 1로 채우기
# print(graph)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
size = 0

for i in range(m) :
    for j in range(n) :
        cnt = dfs(i, j)
        if cnt :
            res.append(cnt)
            size = 0

'''
for i in range(m) :
    for j in range(n) :
        if graph[i][j] == 0 : # 영역으로 구분된 공간일 때
            graph[i][j] = 1
            res.append(bfs(i, j))
'''

print(len(res))
for k in sorted(res) :
    print(k, end=' ')