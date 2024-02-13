# 1932 # DP # Book/q32.py 와 동일한 내용 # 한 번 더 풀이 성공
# 정수 삼각형

# 맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때,
# 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라.
# 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에
# 있는 것 중에서만 선택할 수 있다.
# 삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며,
# 범위는 0 이상 9999 이하이다.

# 첫째 줄에 삼각형의 크기 n(1<=n<=500)이 주어지고, 둘째 줄에서 n+1번째 줄까지 정수 삼각형이 주어진다.

# 예제에서 최대 합의 경로
# 7 -> 3 -> 8 -> 7 -> 5 = 30

# cmd 창 내 input 모양새를 기준으로 보았을 때
# TopDown) 본인 아래 있는 값 & 본인 오른쪽 아래 대각선 중에 내려가면서 선택 가능
# BottomUp) 본인 바로 위 값 & 본인 왼쪽 위 대각선 중에 올라가면서 선택 가능

arr = []
#sum = 0 # 총합 계산용
res = 0
n = int(input())

for i in range(0, n) :
    tmp = list(map(int, input().split()))
    arr.extend(tmp)
# print(arr)

idx = 0
# depth별 첫 번째 값을 저장할 (depth 2부터 시작)
depth = 2
start = 1

# 0               ->1
# 1 2             ->2
# 3 4 5           ->3
# 6 7 8 9         ->4
# 10 11 12 13 14  ->5
# 1) 지금 값 + 다음 depth OR 지금 값 + 현재 depth
# 2) 지금 값 - 이번 depth OR 지금 값 - 다음 depth

while depth <= n :
    for j in range(0, depth) :
        if j == 0 :
            arr[start+j] += arr[start+j-(depth-1)]
        elif j == depth-1 :
            arr[start+j] += arr[start+j-depth]
        else :
            arr[start+j] += max(arr[start+j-depth], arr[start+j-(depth-1)])
        #res = max(res, arr[start+j]) -> 이렇게 풀면 문제 발생. 해당 depth에 따른 순간적인 최댓값때문에 그럴 수도.
        #print(depth, ')', start+j, res)
    start+=depth
    depth+=1

print(max(arr))