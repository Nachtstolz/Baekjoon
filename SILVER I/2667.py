# 2667
# 단지번호 붙이기

# <그림1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려고 한다.
# 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우
# 연결된 것이 아니다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여라.

# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5<=N<=25)이 입력되고 
# 그 다음 N줄에는 각각 N개의 자료(0 혹은 1)가 입력된다.

# 첫 번째 줄에는 총 단지 수를 출력, 각 단지 내 집의 수를 오름차순 정렬해 한 줄에 하나씩 출력한다.

# DFS/BFS

n = int(input())
arr = []
check = [[0] * n for _ in range(n)]
for _ in range(n) :
    tmp = list(map(int, input()))
    arr.append(tmp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, house, li) :
    for i in range(4) :
        nx = x+dx[i]
        ny = y+dy[i]
        # 집이 있는 곳이면서 방문하지 않은 곳일 때
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1 and check[nx][ny] == 0 :
            house+=1
            check[nx][ny] = 1
            #print(nx, ny, house)
            li.append(house)
            dfs(nx, ny, house, li)

town = 0
res = []
for i in range(n) :
    for j in range(n) :
        if arr[i][j] == 1 and check[i][j] == 0 :
            check[i][j] = 1
            town += 1
            house = 1
            li = []
            dfs(i, j, house, li)
            # print(li)
            # print(li[-1])
            # print(town, li[-1])
            #print(town, house)
            if len(li) > 0 :
                res.append(li[-1])
            else :
                res.append(house)

res.sort()
print(town)
for i in res :
    print(i)
