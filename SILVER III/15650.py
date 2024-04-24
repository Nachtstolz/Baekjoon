# 15650 # 성공!
# N과 M(2)

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하라.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.

# 첫째 줄에 자연수 N과 M이 주어진다. (1<=M<=N<=8)
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력. 중복되는 수열을 여러 번 출력하며 안되며, 각 수열은 공백으로 구분해서 출력
# 수열은 사전 순으로 증가하는 순서로 출력해야 함.

from itertools import combinations
n, m = map(int, input().split())
arr = []
for i in range(1, n+1) :
    arr.append(i)
nCm = list(combinations(arr, m))

#print(list(nCm))
for item in nCm :
    if len(item) == 1 :
        print(item[0], end='')
    else :
        for i in range(len(item)) :
            print(item[i], end=' ')
    print()
    