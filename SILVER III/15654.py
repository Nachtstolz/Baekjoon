# 15654 # 성공 # 백트래킹 사용 방법 추가 완료
# N과 M (5)

# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# N개의 자연수는 모두 다른 수이다. * N개의 자연수 중에서 M개를 고른 수열
# 첫째 줄에 N과 M이 주어진다. (1<=M<=N<=8)
# 둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며,
# 각 수열은 공백으로 구분해서 출력한다. 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

'''

from itertools import permutations
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

res = list(permutations(arr, m))
for each in res :
    for j in range(m) :
        print(each[j], end=' ')
    print() 
'''

''' 백트래킹 방법 사용 '''

# 깊이가 M이 될 때, 주어진 숫자들을 탐색하기.
# 순열, 중복되지 않은 숫자들을 나열해야 하므로 이미 추가된 숫자가 있다면 continue 할 것.

n, m = map(int, input().split())
numbers = [int(x) for x in input().split()] # 배열에 숫자 받기
numbers.sort()

def backtracking(depth) :
    if depth == m :
        print(' '.join(map(str,box))) # 배열 box를 문자열 형태로 출력(숫자이기에 문자열인 배열로 바꾸고), 공백 구분자
        return
    
    for i in range(n) :
        if numbers[i] in box : # 이미 넣은 값이면 제외
            continue
        box.append(numbers[i])
        backtracking(depth+1)
        box.pop()

box = []
backtracking(0)
