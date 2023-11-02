# 1920 # 정답!
# 수 찾기

# N개의 정수 A[1], A[2], ... A[N]이 주어졌을 때, 이 안에 X라는 정수가
# 존재하는지 알아내는 프로그램을 작성하시오.

# 첫째 줄에 자연수 N(1 <= N <= 100,000)이 주어진다. 다음 줄에는 N개의 정수
# A[1], A[2], ... A[N]이 주어진다.
# 다음 줄에는 M(1 <= M <= 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데
# 이 수들이 A 안에 존재하는지 알아내면 된다.
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

def search(li, topic, start, end) :
    #print(start, end)
    if end < start :
        return 0

    mid = (end+start)//2
    if li[mid] == topic :
        return 1
    elif li[mid] > topic :
        return search(li, topic, start, mid-1)
    else :
        return search(li, topic, mid+1, end)

n = int(input())
list_n = list(map(int, input().split(' ')))
m = int(input())
list_m = list(map(int, input().split(' ')))

# n 리스트 정렬하기
list_n.sort()

# m 리스트까지 정렬하면 더 좋을텐데....
# 이진 탐색
res = []
for i in list_m :
    tmp = search(list_n, i, 0, n-1)
    res.append(tmp)

for i in res :
    print(i)
