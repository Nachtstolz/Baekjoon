# 11723 # 비트마스크 # 성공 # 비트연산 서치 -> 풀이
# 집합

# 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.
# add x : S에 x를 추가 (1<=x<=20) S에 x가 이미 있는 경우에는 연산 무시
# remove x : S에서 x를 제거 (1<=x<20) S에 x가 없는 경우에는 연산 무시
# check x : S에 x가 있으면 1을, 없으면 0을 출력 (1<=x<=20)
# toggle x : S에 x가 있으면 x를 제거하고, 없으면 x를 추가 (1<=x<=20)
# all : S를 {1,2,...,20}으로 바꿈
# empty : S를 공집합으로 바꿈

# 첫째 줄에 수행해야 하는 연산의 수 M(1<=M<=3,000,000)이 주어진다.
# 둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

# check 연산이 주어질 때마다, 결과를 출력한다.



# 풀이 1 : 단순 구현
'''
m = int(input())
res = set()
while m > 0 :
    m-=1
    x = 0
    # 연산 기반 명령어, x 분리 작업
    cal = input()
    if cal.count(' ') >= 1 :
        cal, x = cal.split(' ')
        x = int(x)
    # print(cal, x, x+1)

    if cal == 'add' :
        res.add(x)
    elif cal == 'remove' :
        res.discard(x)
    elif cal == 'check' :
        if x in res :
            print(1)
        else :
            print(0)
    elif cal == 'toggle' :
        if x in res :
            res.remove(x)
        else :
            res.add(x)
    elif cal == 'all' :
        res = set({1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20})
    elif cal == 'empty' :
        res.clear()
'''

# 풀이 2 : 알고리즘 참고 -> 비트마스킹

import sys
input = sys.stdin.readline

m = int(input().strip())
res = 0 # 비트마스크를 진행할 숫자

while m > 0 :
    m-=1
    x = 0

    # 연산 기반 명령어, x 분리 작업
    cal = input().strip() # strip을 해야 개행문제 제거 가능
    if cal.count(' ') >= 1 :
        cal, x = cal.split(' ')
        x = int(x)
    # print(cal, x, x+1)

    if cal == 'add' :
        res |= 1<<x # res = res OR (x만큼 1을 좌shift)
    elif cal == 'remove' :
        res &= ~(1<<x) # res = res AND NOT(x만큼 1을 좌shift)
    elif cal == 'check' :
        if res&(1<<x) :
            print(1) # 있으면 1 AND 1, 없으면 0 AND 1의 결과 출력
        else :
            print(0)
    elif cal == 'toggle' :
        res ^= (1<<x) # res = res XOR(둘 중 하나만 1이어야 1출력) x만큼 1을 좌shift
        # 둘 다 1이면 0이되고, 하나만 1이면 1이 되도록.
    elif cal == 'all' :
        res = (1<<21)-1
    elif cal == 'empty' :
        res = 0
