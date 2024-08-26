# 5430 # 구현 # 자료구조(큐, 스택) # 성공
# AC

# 선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. AC는 정수 배열에 연산을 하기 위해 만든 언어이다.
# 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.
# 함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고, D는 첫 번째 수를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는
# 에러가 발생한다. 함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음 이어서 B를 수행하는 함수이다.
# 예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 수를 버리는 함수이다.
# 배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.
# 각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.
# 다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0<=n<=100,000)
# 다음 줄에는 [x1, ..., xn]과 같은 형태로 배열에 들어있는 정수가 주어진다. (1<=xi<=100)
# 전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.

# 각 테스트 케이스에 대해서, 입력으로 주어진 정수 배열에 함수를 수행한 결과를 출력한다. 만약, 에러가 발생하면 error 출력.

# 풀이 1.
# R -> 스택
# D -> 큐

# 16%에서 시간초과

# + reverse 대신 커서 넣기
# + li로 인한 소요 시간으로 queue로 변경 -> 슬라이싱 대신 deque의 pop, popleft

from collections import deque

t = int(input()) # 테스트 케이스의 개수
for _ in range(t) :
    # 입력 구간
    p = list(input()) # 수행할 함수
    # print(p)
    n = int(input()) # 배열에 들어있는 수의 개수

    if n > 0 :
        li = list(map(int, input()[1:-1].split(',')))
    else :
        input() # 아무 입력이나 받고
        li = list() # 빈 리스트 돌려주기
    # print(li)
    q = deque(li)
    # print(q)

    # 함수 수행 구간
    error = False
    cursor = 1 # 앞을 바라볼 때 1, 뒤를 바라볼 때 -1
    for func in p :
        #print(func, li)
        if error == True :
            break

        if func == 'R' : # 뒤집기
            # li.reverse() # 나중에 시간 보고 수정하기
            if cursor == -1 :
                cursor = 1
            else :
                cursor = -1
        else : # 커서 확인 -> 첫 번째 수를 버리기
            if len(q) < 1 : # 배열 길이 기반으로 error 체크
                error = True
                continue

            if cursor == 1 : # 앞에서 삭제
                #li = li[1:]
                q.popleft()
            else : # 뒤에서 삭제
                #li = li[:-1]
                q.pop()

        #print(li)

    # 출력 구간
    if error == True :
        print("error")
    else :
        print('[',end='')
        if cursor == -1 :
            #li.reverse()
            while len(q) :
                if len(q) <= 1 :
                    print(q.pop(),end='')
                else :
                    print(q.pop(),end=',')
        else :
            while len(q) :
                if len(q) <= 1 :
                    print(q.popleft(),end='')
                else :
                    print(q.popleft(),end=',')
        print(']')

