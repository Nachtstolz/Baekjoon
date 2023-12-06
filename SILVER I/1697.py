# 1697 # BFS # 인터넷 서치 # 추후 재도전
# 숨바꼭질

# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0<=N<=100,000)에 있고,
# 동생은 점 K(0<=K<=100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다.
# 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지
# 구하는 프로그램을 작성하라.

# 첫째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

from collections import deque
MAX = 100001
n, k = map(int, input().split())
depth = [0] * MAX # 나오는 수의 깊이 표시를 위한 배열

q = deque([n])
while q :
    num = q.popleft()
    if num == k :
        print(depth[num])
        break
    for next in (num-1, num+1, 2*num) :
        if 0 <= next < MAX and depth[next] == 0 :
            depth[next] = depth[num] + 1
            q.append(next)