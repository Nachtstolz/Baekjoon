# 15652 # 백트래킹 # 정답 - 조합 함수로 풀이
# N과 M(4)

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다. (길이가 K인 수열 A가 A1<=A2<=...<=Ak-1<Ak를 만족하면, 비내림차순)

# 첫째 줄에 자연수 N과 M이 주어진다. (1<=M<=N<=8)
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서
# 출력해야 한다. 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

# 조합 : combinations
# 중복조합 : combinations_with_replacement
'''
from itertools import combinations_with_replacement

n, m = map(int, input().split())
li = combinations_with_replacement(range(1, n+1), m)
for i in li :
    for j in i :
        print(j, end=' ')
    print()
'''

# 백트래킹(퇴각 검색) : 길을 가다가 이 길이 아닌 것 같으면 왔던 기로 되돌아가 다른 경로로 진행
# 보통 재귀로 구현, 조건이 맞지 않으면 종료.
# DFS(깊이 우선 탐색) 기반
# 인터넷 서치 코드 기록
n, m = map(int, input().split())
s = []

def dfs(start) :
    if len(s) == m :
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, n+1) :
        s.append(i)
        dfs(i)
        s.pop()

dfs(1)