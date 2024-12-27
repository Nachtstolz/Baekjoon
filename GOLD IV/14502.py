# 14502 # 유사문제 많음 # 성공! # 다른 풀이 추가 예정
# 연구소 

# 인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을
# 막기 위해서 연구소에 벽을 세우려고 한다. 연구소는 크기가 NxM인 직사각형으로 나타낼 수 있으며, 직사각형은 1x1 크기의 정사각형으로
# 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며 벽은 칸 하나를 가득 차지한다.
# 일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는
# 3개이며, 꼭 3개를 세워야 한다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다.
# 벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 연구소의 지도가 주어졌을 때, 얻을 수 있는 안전 영역 크기의
# 최댓값을 구하는 프로그램을 작성하시오.

# 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3<=N, M<=8)
# 둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다.
# 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다. 빈칸의 개수는 3개 이상이다.

# 1. 0의 위치 추출 -> combinatinos로 조합 구해서 그 위치에 벽 놓으면서 최댓값 찾기
# bfs 활용하기

from itertools import combinations
from collections import deque
import time

n, m = map(int, input().split())
graph = [] # 지도 값 저장
zero = [] # 벽을 세울 수 있는 빈 칸의 인덱스 저장하기
virus = []
res = 0
# virus가 퍼져나갈 x, y 좌표
v_x = [-1, 1, 0, 0] 
v_y = [0, 0, -1, 1]

for i in range(n) :
    tmp = list(map(int, input().split()))
    # 0, 2 위치 바로 찾아서 저장하기
    for j in range(len(tmp)) :
        if tmp[j] == 0 :
            zero.append((i,j))
        elif tmp[j] == 2 :
            virus.append((i,j))
    graph.append(tmp)

zero_comb = list(combinations(zero, 3))
# print(zero_comb)
for walls in zero_comb :
    for idx in range(3) :
        a, b = walls[idx]
        #print(a,b)
        graph[a][b] = 1
    # print(graph)

    q = deque(virus) # 기존 virus로 queue 배열 만들기
    graph_cp = [[0] * m for _ in range(n)] # 여기에 바이러스 확산 표시. 추후 graph랑 and 연산자를 통해 안전 확인
    while q :
        # time.sleep(1)
        #print(q)
        x, y = q.popleft()
        for i in range(4) :
            ax = x+v_x[i]
            ay = y+v_y[i]
            if ax >= 0 and ax < n and ay >= 0 and ay < m :
                # print((ax, ay))
                if graph[ax][ay] == 0 and graph_cp[ax][ay] == 0 :
                    q.append((ax, ay))
                    graph_cp[ax][ay] = 1
                else :
                    continue
    # print(graph_cp)

    tmp = 0 # res와 비교할 값
    for x in range(n) :
        for y in range(m) :
            if graph[x][y] == 0 and graph_cp[x][y] == 0 :
                tmp += 1
    res = max(res, tmp)

    for idx in range(3) :
        a, b = walls[idx]
        graph[a][b] = 0

print(res)
    