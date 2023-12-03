# 2606 # 바이러스 # 그래프 이론 풀이

# 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면
# 그 컴퓨터와 네트워크 상 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
# 어느 날, 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상 서로 연결된
# 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하라.

# 첫째 줄에 컴퓨터의 수가 주어진다. 100 이하의 양의 정수이고 각 컴퓨터는 1번부터 차례대로
# 번호가 매겨진다. 둘째 줄에는 네트워크 상 직접 연결된 컴퓨터 쌍의 수가 주어진다.
# 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상 직접 연결된 컴퓨터의 번호 쌍이 주어진다.

# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를
# 출력하라.

def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
 
def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

node = int(input())
line = int(input())
parent = [0] * (node+1)

for i in range(1, node+1) : # parent 배열 초기화. 본인으로.
    parent[i] = i


for _ in range(line) : # 간선 간 연결 입력
    a, b = map(int, input().split())
    union_parent(parent, a, b)

cnt = 0
for i in range(1, node+1) :
    # 마지막에 한 번 더 find_parent 해줘야.
    if find_parent(parent, i) == 1 :
        cnt+=1

print(cnt-1)