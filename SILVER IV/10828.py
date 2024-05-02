# 10828 # 성공!
# 스택

# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 명령은 총 다섯 가지이다.
# push X : 정수 X를 스택에 넣는 연산
# pop : 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력. 만약 스택에 들어있는 정수가 없는 경우 -1 출력
# size : 스택에 들어있는 정수의 개수를 출력
# empty : 스택이 비어있으면 1, 아니면 0을 출력
# top : 스택의 가장 위에 있는 정수를 출력. 만약 스택에 들어있는 정수가 없는 경우 -1 출력

# 첫째 줄에 주어지는 명령의 수 N(1<=N<=10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
# 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
# 출력해야하는 명령이 주어질 때마다 한 줄에 하나씩 출력한다.

import sys

n = int(sys.stdin.readline())
stack = []
for i in range(n) :
    cmd = list(sys.stdin.readline())
    tmp = ''.join(cmd[:2])
    if tmp == 'pu' : # push 명령어
        num = int(''.join(cmd[5:]))
        stack.append(num)
    elif tmp == 'po' : # pop 명령어
        if len(stack) > 0 :
            print(stack[-1])
            stack.pop(-1)
        else :
            print(-1)
    elif tmp == 'si' : # size 명령어
        print(len(stack))
    elif tmp == 'em' : # empty 명령어
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
    elif tmp == 'to' : # top 명령어
        if len(stack) > 0 :
            print(stack[-1])
        else :
            print(-1)