# 1931 # 정렬 # 그리디 # 인터넷 풀이 참고 # 성공
# 회의실 배정

# 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만드려고 한다.
# 각 회의 I에 대해 시작 시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의
# 최대 개수를 찾아보자. 단, 회의는 한 번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가
# 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

# 첫째 줄에 회의이 수 N(1<=N<=100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데
# 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다.
# 시작시간과 끝나는 시간은 2의 31승-1보다 작거나 같은 자연수 또는 0이다.

# 첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.
# 회의실은 한 개. 최대 몇 개의 회의를 할 수 있는지.


'''
def func(k, arr, tmp, res) :
    for i in range(n) :
        if arr[i][0] >= k :
            print(arr[i][0], arr[i][1])
            tmp+=1
            return func(arr[i][1], arr, tmp, res)
    res = max(res, tmp)
            

n = int(input())
arr = []
result = 1

for i in range(n) :
    a, b = map(int, input().split())
    arr.append((a,b))
arr.sort()
print(arr)

for i in range(n):
    start = arr[i]
    print(start[0], start[1])
    tmp = res = 1
    print('//////%d//////' %i)
    debug = func(start[1], arr, tmp, res)
    print('res : ', debug)
    result = max(debug, result)
    
print(result)
'''

# (1) 빨리 끝나는 회의 순서대로 정렬을 해야 -> 빨리 끝날수록 뒤에서 고려해볼 회의가 많기 때문.
# 빨리 시작하는 순서대로 정렬 -> 오히려 늦게 끝날 수 있음.
# 간단한 예)
# 4
# 0 10
# 3 4
# 2 3
# 1 2
# 시작 순서대로 하면 (0,10)으로 1번의 회의가 끝나지만, 끝나는 시간으로 정렬하면 (1,2) (2,3), (3,4) 총 3번 가능.

# (2) 끝나는 시간이 같을 경우, 빨리 시작하는 순서대로 정렬해야.
# 간단한 예)
# 2
# 2 2
# 1 2
# 의 경우 이 상태로 한다면 (2,2)가 되고 (1,2)는 (2,2)의 끝나는 시간보다 시작 시간이 일찍이어서 무시 -> 1번 회의 가능
# 정렬을 통해 (1,2)가 먼저 선택되면 (2,2)도 선택이 가능 -> 2번 회의 가능
# [결론] 1. 끝나는 시간의 오름차순 2. 시작하는 시간의 오름차순으로 정렬해야.

n = int(input())
arr = []
result = 1

for i in range(n) :
    a, b = map(int, input().split())
    arr.append((a,b))

arr.sort(key=lambda x:(x[1], x[0]))
# print(arr)

result = 0
next = 0
for start, end in arr :
    if start >= next :
        next = end
        result+=1
print(result)
