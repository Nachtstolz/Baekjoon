# 12891 # 슬라이딩윈도우 # 딕셔너리 # 성공
# DNA 비밀번호

# 평소에 문자열을 가지고 노는 것을 좋아하는 민호는 DNA 문자열을 알게 되었다. DNA 문자열은 모든 문자열에 등장하는 문자가 
# {'A', 'C', 'G', 'T'}인 문자열을 말한다. 예를 들어 "ACKA"는 DNA문자열이 아니지만, "ACCA"는 DNA 문자열이다.
# 이런 신비한 문자열에 완전히 매료된 민호는 임의의 DNA 문자열을 만들고 만들어진 DNA 문자열의 부분문자열을 비밀먼호로 사용하기로 했다.

# 하지만 민호는 이러한 방법에 큰 문제가 있다는 것을 발견했다. 임의의 DNA 문자열의 부분문자열을 뽑았을 때 "AAAA"와 같이 보안에
# 취약한 비밀번호가 만들어질 수 있다. 그래서 부분문자열에서 등장하는 문자의 개수가 특정 개수 이상이여야 비밀번호로 사용할 수 있다.
# 임의의 DNA 문자열이 "AAACCTGCCAA"이고 민호가 뽑은 문자열의 길이가 4라고 하자.
# 그리고 'A'는 1개 이상, 'C'는 1개 이상, 'G'는 1개 이상, 'T'는 0개 이상이 등장해야 비밀번호로 사용할 수 있다고 하자.
# 이때 "ACCT"는 'G'가 1개 이상 등장해야 한다는 조건을 만족하지 못해 비밀번호로 사용할 수 없다.
# 하지만 "GCCA"는 모든 조건을 만족하기에 비밀번호로 사용할 수 있다.
# 민호가 만든 임의의 DNA 문자열과 비밀번호로 사용할 부분문자열의 길이, 그리고 {'A', 'C', 'G', 'T'}가 각각 몇 번 이상 등장해야
# 비밀번호로 사용할 수 있는지 순서대로 주어졌을 때 민호가 만들 수 있는 비밀번호의 종류 수를 구하는 프로그램을 작성하자.
# 단 부분문자열이 등장하는 위치가 다르다면 부분문자열이 같다고 하더라고 다른 문자열로 취급한다.

# 첫째 줄에 민호가 만든 DNA 문자열 길이 |S|와 비밀번호로 사용할 부분문자열의 길이 |P|가 주어진다. (1<=|P|<=|S|<=1,000,000)
# 둘째 줄에는 민호가 임의로 만든 DNA 문자열이 주어진다.
# 셋째 줄에는 부분문자열에 포함되어야 할 {'A', 'C', 'G', 'T'}의 최소 개수가 공백을 구분으로 주어진다.
# 각각의 수는 |S|보다 작거나 같은 음이 아닌 정수이며 총 합은 |S| 보다 작거나 같음이 보장된다.

# 첫째 줄에 민호가 만들 수 있는 비밀번호의 종류 수를 출력해라.

# from itertools import combinations
import sys
input = sys.stdin.readline
s, p = map(int, input().split())
li = list(input())
a, c, g, t = map(int, input().split())
res = 0

left = 0
right = p

# 처음 주어지는 길이에 맞게 계산
cnt = {'A' : 0, 'C': 0, 'G': 0, 'T': 0}
first = li[:right] # 첫번째 구간
for i in first :
    if i == 'A' :
        cnt['A']+=1
    elif i == 'C' :
        cnt['C']+=1
    elif i == 'G' :
        cnt['G']+=1
    elif i == 'T' :
        cnt['T']+=1

    if cnt['A']>=a and cnt['C']>=c and cnt['G']>=g and cnt['T']>=t :
        res+=1

for i in range(abs(s)-abs(p)) : # 처음 계산 빼서 +1 안함
    # part = li[i:length] # 이중for문 구조가 되어 시간초과
    # 기존문자열인덱스+1 값은 더해주고, 기존시작문자열인덱스 값은 빼주고 -> 자연스러운 슬라이딩 윈도우 진행
    remove = li[left]
    add = li[right]

    if remove == 'A' :
        cnt['A']-=1
    elif remove == 'C' :
        cnt['C']-=1
    elif remove == 'G' :
        cnt['G']-=1
    elif remove == 'T' :
        cnt['T']-=1

    if add == 'A' :
        cnt['A']+=1
    elif add == 'C' :
        cnt['C']+=1
    elif add == 'G' :
        cnt['G']+=1
    elif add == 'T' :
        cnt['T']+=1

    if cnt['A']>=a and cnt['C']>=c and cnt['G']>=g and cnt['T']>=t :
        res+=1

    left+=1
    right+=1

print(res)
