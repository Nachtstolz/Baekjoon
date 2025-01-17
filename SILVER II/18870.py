# 18870 # 성공 # 정렬 # 해시
# 좌표 압축

# 수직선 위에 N개의 좌표 X1, X2, ..., Xn이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.
# X1, X2, ..., Xn에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'n을 출력해보자.

# 첫째 줄에 n이 주어진다. 둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., Xn이 주어진다.
# 첫째 줄에 X'1, X'2, ..., X'n을 공백 한 칸으로 구분해서 출력한다.
# [ 제한 사항 ]
# 1<=N<=1,000,000
# -10의 9승 <= Xi <= 10의 9승

# 문제 이해 정리
# 주어진 좌표들 중, Xi의 값보다 작은 값들의 개수를 각각 출력하라 : X'i

import sys
input = sys.stdin.readline


# sort -> 불가능
# 직접 다 비교 -> 불가능

# merge sort 같은 걸로 가능한지 : 다른 정렬 방법 사용
n = int(input())
arr = list(map(int, input().split()))

cmp = list(set(arr))
def merge_sort(arr) :
    if len(arr) < 2 :
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    l = r = 0
    while l < len(left) and r < len(right) :
        if left[l] < right[r] :
            merged.append(left[l])
            l+=1
        else :
            merged.append(right[r])
            r+=1
    merged += left[l:]
    merged += right[r:]
    return merged

res = merge_sort(cmp)
# 인덱스 찾는 접근은 시간 초과
# for i in range(len(arr)) :
#     print(res.index(arr[i]), end=' ') 

dic = {}
for i in range(len(res)) :
    dic[res[i]] = i

for i in arr :
    print(dic[i], end = " ")


