# 1012 # dfs/bfs # 성공!
# 유기농 배추

# 차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 했다.
# 해충 방지에 효과적인 배추흰지렁이를 구입하기로 했는데, 이 지렁이는 배추 근처에 서식하며 해충을 잡아먹음으로써
# 배추를 보호한다. 특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로
# 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다.
# 한 배추는 상하좌우 네 방향에 다른 배추가 위치한 경우 인접해있다고 할 수 있다.
# 한나가 배추를 군데군데 심어놓았고 배추들이 모여있는 곳에 배추흰지렁이가 한 마리만 있으면 되므로
# 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리가 필요한지 알 수 있다.
# 0은 배추가 심어있지 않은 땅을, 1은 배추가 심어져있는 땅을 나타낸다.

# 입력 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해
# 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1<=M<=50)과 세로길이 N(1<=N<=50) 그리고 배추가 심어져있는
# 위치의 개수 K(1<=K<=2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0<=X<=M-1), Y(0<=Y<=N-1)가 주어진다.
# 두 배추의 위치가 같은 경우는 없다.

# 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

import sys
sys.setrecursionlimit(10**6) # RecursionError를 벗어나기 위한

def dfs(graph, x, y) :
    for i in range(4) : # 상하좌우 이동
        ax = x+dx[i]
        ay = y+dy[i]
        # 범위를 벗어나지 않으면서 들른 적 없고, 배추가 심어져 있으면
        if 0<=ax<m and 0<=ay<n and graph[ay][ax] == 1 and check[ay][ax] == 0 :
            check[ay][ax] = 1
            dfs(graph, ax, ay)

t = int(input()) # 테스트 케이스
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while t>0 :
    t-=1
    m, n, k = map(int, input().split()) # 가로, 세로, 배추 개수
    graph = [[0] * m for _ in range(n)] # 배추가 있는 위치 저장
    check = [[0] * m for _ in range(n)] # 들렀는지 확인하기 위한 배열
    for i in range(k) :
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    res = 0
    for i in range(n) :
        for j in range(m) :
            if graph[i][j] == 1 and check[i][j] == 0 :
                dfs(graph, j, i)
                res+=1

    print(res)