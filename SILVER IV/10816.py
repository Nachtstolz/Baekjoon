# 10816 # 자료구조 # 정렬 # 이분탐색 # 해시를 사용한 집합과 맵 # 성공
# 숫자 카드 2

# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1<=N<=500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는
# 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
# 셋째 줄에는 M(1<=M<=500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의
# 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

# 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력.

# 배열에 일일히 저장 X -> 너무 숫자가 커짐
# ⭐️ 시간 초과 이유 : 1을 찾아야 하고, 1이 10만개 있을 경우에 대한 확인 반복 -> 많은 시간 소요 O(N) ⭐️
# ⭐️ 딕셔너리 사용 -> 딕셔너리가 탐색하는데 O(1)의 시간이 걸린다는 정보 입수 ⭐️
# ⭐️ 파이썬에서 hash를 딕셔너리를 사용해 구현 가능 ⭐️

# 시간 초과 코드
'''
def count_check(arr, topic, idx) :
    cnt = 0
    # 작은 인덱스로 이동
    for i in range(idx, -1, -1) :
        if arr[i] == topic :
            cnt+=1

    # 큰 인덱스로 이동
    for i in range(idx, len(arr)) :
        if arr[i] == topic :
            cnt+=1

    # print(cnt)
    return cnt-1 # 중복되는 값 제거
'''

def binary_search(arr, topic, start, end) :
    if start > end :
        return 0
    
    mid = (start+end) // 2
    # print("%d : %d %d %d" %(topic, start, end, mid))
    if arr[mid] == topic :
        return dic[topic]
    elif arr[mid] > topic :
        return binary_search(arr, topic, start, mid-1)
    else :
        return binary_search(arr, topic, mid+1, end)


n = int(input())
arr = sorted(list(map(int, input().split())))
# print(arr)

# 딕셔너리에 저장
dic = {}
for key in arr :
    if key in dic :
        dic[key]+=1
    else :
        dic[key] = 1

m = int(input())
search = list(map(int, input().split()))

for i in range(m) :
    print(binary_search(arr, search[i], 0, n-1), end=' ')

''' 다른 풀이 방법 1 - 인터넷 서치 결과 '''
# 딕셔너리 사용. 이분 탐색 X

import sys
input = sys.stdin.readline

N = int(input())
N_s = list(map(int, input().split()))
M = int(input())
M_s = list(map(int, input().split()))

n_dic = {}

for n in N_s :
    if n in n_dic :
        n_dic[n] += 1
    else :
        n_dic[n] = 1

for m in M_s :
    if m in n_dic :
        print(n_dic[m], end=' ')
    else :
        print(0, end=' ')

''' 다른 풀이 방법 2 - 인터넷 서치 결과 '''
# collections 라이브러리의 Counter 함수 사용

# Counter 생성자는 여러 형태의 데이터를 인자로 받아, 중복된 데이터가 저장된 배열을 인자로 넘기면 각 원소가 
# 몇 번씩 나오는 지가 저장된 객체를 얻게 된다. 문자열을 인자로 넘기면 각 문자가 문자열에서 몇 번씩 나타나는지 알려준다.
# 가장 많이 나온 데이터를 구하려면 Counter('hello world').most_common(1)을 통해 구한다.

# Counter 클래스는 각 숫자 카드의 개수를 셀 수 있다. 입력값을 순회하몋 연산을 수행하므로 N개의 원소를 가진 리스트를 한번
# 순회하면서 Counter 객체를 구성하는 데 O(N) 시간이 걸린다. 그리고 M개의 값을 가진 리스트를 순회하며 Counter 객체에서
# 값을 찾아 출력하므로, 이 과정에서도 O(M) 시간이 걸린다. -> O(N+M)
from sys import stdin
from collections import Counter

_ = stdin.readline()
N = stdin.readline().split()
_ = stdin.readline()
M = stdin.readline().split()

# 카드 수 세기
C = Counter(N)

print(' '.join(f'{C[m]}' if m in C else '0' for m in M))
