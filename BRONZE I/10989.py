# 10989 # 성공 # 
# 수 정렬하기 3

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 첫째 줄에 수의 개수 N(1<=N<=10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다.
# 이 수는 10,000보다 작거나 같은 자연수이다.
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 풀이1) 머지소트
# n = int(input())
# arr = []
# for _ in range(n) :
#     arr.append(int(input()))

# def merge_sort(arr) :
#     if len(arr) < 2 :
#         return arr
    
#     mid = len(arr) // 2
#     low_arr = merge_sort(arr[:mid])
#     high_arr = merge_sort(arr[mid:])

#     merged_arr = []
#     l = h = 0
#     while l < len(low_arr) and h < len(high_arr) :
#         if low_arr[l] < high_arr[h] :
#             merged_arr.append(low_arr[l])
#             l+=1
#         else :
#             merged_arr.append(high_arr[h])
#             h+=1

#     merged_arr += low_arr[l:]
#     merged_arr += high_arr[h:]
#     return merged_arr

# arr = merge_sort(arr)
# for i in range(n) :
#     print(arr[i])

# 풀이2) 배열 append 최소화 -> 메모리 초과 줄이기 위함
import sys

input = sys.stdin.readline
n = int(input())
arr = [0] * 10001 # 개수 체크 -> 개수만큼 출력하는 방식
for i in range(n) :
    # tmp = int(input())
    arr[int(input())]+=1

for i in range(10001) :
    if arr[i] > 0 :
        # 문자형으로 만들어서 반복 출력할 수 있도록
        for _ in range(arr[i]) :
            print(i)
        # print('{0}\n'.format(i)*arr[i], end='')

# 풀이3) 계수정렬로 가능하다고 함 -> 노션에 정리