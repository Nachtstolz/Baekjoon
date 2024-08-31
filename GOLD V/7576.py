# 7576 # BFS # 정답 
# 토마토

# C 구현 -> 틀렸습니다

# 철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 
# 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 상자에 보관한다.
# 창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면,
# 익은 토마토들의 인접한 곳에 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
# 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는
# 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면
# 다 익게 되는지, 그 최소 일수를 알고 싶어한다.
# 토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때,
# 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지
# 않을 수도 있다.

# 첫 줄에는 상자의 크기를 나타내는 두 정수 M, N이 주어진다. M은 상자의 가로 칸 수, N은 상자의 세로 칸 수를 나타낸다.
# 단 2 <= M,N <= 1,000이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다.
# 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가
# M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
# 토마토가 하나 이상 있는 경우만 입력으로 주어진다.

# 여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을,
# 토마토가 모두 익지 못하는 상황이면 -1을 출력해야 한다.

from collections import deque

m, n = map(int, input().split())
arr = []
complete = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
col = 0
day = 0 # 며칠 걸리는지 확인하기 위한 변수

for i in range(n) :
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    for j in range(m) :
        if tmp[j] == 1 :
            complete.append((day, col, j)) # 날짜, 익은 토마토의 x좌표, 익은 토마토의 y좌표
    col += 1
#print(arr)


# 박스 내 토마토가 모두 익었는지 체크
cnt_zero = 0
for i in range(n) :
    cnt_zero += arr[i].count(0)

if cnt_zero < 1 :
    print(day)
    exit(0)

# BFS -> 큐
# complete에 넣어놓은 값을 기반으로 하나씩 추출(pop) -> 새로 익은 애들 다시 넣는 방식으로(push)
def bfs(day) : 
    q = deque(complete)

    # (시간 문제 발생 시 진행 예정) 처음 익은 토마토 수 저장 -> 마지막에 이 수를 전체 배열 크기와 비교하는 방법
    # 일단 count를 사용해서 진행 예정
    # cnt_complete = len(complete) 
    #print(q)

    while len(q)>0 : # 큐에 아무것도 없을 때까지
        #print(q)
        day += 1
        q_size = len(q)
        for _ in range(q_size) : 
            top = q.popleft()
            #print(top)
            for i in range(4) : # 상하좌우 1로 변경
                tx = top[1]+dx[i]
                ty = top[2]+dy[i]
                if 0 <= tx < n and 0 <= ty < m :
                    if arr[tx][ty] == 0 :
                        arr[tx][ty] = 1
                        q.append((day, tx, ty)) # 새로 익은 토마토
                        #cnt_complete += 1
        

    cnt_zero = 0
    for i in range(n) :
        cnt_zero += arr[i].count(0)

    if cnt_zero > 0 :
        print(-1)
    else :
        print(day-1)

bfs(day)