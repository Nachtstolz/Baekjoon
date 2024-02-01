# 2751 # 성공! # 퀵 정렬, 병합 정렬 코드 한 번씩 보기
# 실제로 해결 방식 : sys 사용하기 (허탈했지만...)
# 수 정렬하기 2

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하라.
# 첫째 줄에 수의 개수 N(1<=N<=1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는
# 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

import sys
n = int(sys.stdin.readline())
li = []
for _ in range(n) :
    li.append(int(sys.stdin.readline()))

# 퀵 정렬 코드
def quick_sort(li) :
    if len(li) <= 1 :
        return li
    pivot = len(li) // 2
    left, right, equal = [], [], []
    for i in li :
        if i < li[pivot] :
            left.append(i)
        elif i > li[pivot] :
            right.append(i)
        else :
            equal.append(i)

    return quick_sort(left) + equal + quick_sort(right)

# 병합 정렬 코드
def merge_sort(li) :
    if len(li) < 2 :
        return li
    mid = len(li) // 2
    left = merge_sort(li[:mid])
    right = merge_sort(li[mid:])

    res = []
    l = r = 0
    while l < len(left) and r < len(right) :
        if left[l] < right[r] :
            res.append(left[l])
            l+=1
        else :
            res.append(right[r])
            r+=1
    res += left[l:]
    res += right[r:]
    #print(res)
    return res

li.sort() # sys.stdin.readline() 하고나니 가능해짐..ㅋㅋ
li = merge_sort(li)
for i in range(n) :
    print(li[i])