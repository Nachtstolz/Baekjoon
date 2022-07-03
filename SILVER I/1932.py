# 1932
# 정수 삼각형

# 맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때,
# 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라.
# 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에
# 있는 것 중에서만 선택할 수 있다.
# 삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며,
# 범위는 0 이상 9999 이하이다.

# 첫째 줄에 삼각형의 크기 n(1<=n<=500)이 주어지고, 둘째 줄에서 n+1번째 줄까지 정수 삼각형이 주어진다.

arr = []
sum = 0 # 총합 계산용
n = int(input())

for i in range(0, n) :
    print('i : ', i)
    # 하는 중
    #map(int, input().split())
    #arr.append()
    '''
    for j in range(0, i+1) :
        print('j : ',j)
        arr.append(int(input()))
    '''
print(arr)

depth = 1
idx = 0
for j in range(n) :
    max = 0
    for i in range(depth) :
        if max < arr[idx+i] :
            max = arr[idx+i]
    idx+=depth #idx 변경
    sum+=max #sum에 depth에 따른 max값 추가

print(sum)