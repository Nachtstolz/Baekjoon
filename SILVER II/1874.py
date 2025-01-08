# 1874 # 스택 # 성공
# 스택 수열

# 스택은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 스택은 자료를 넣는(push) 입구와
# 자료를 뽑는(pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 LIFO 특성을 가지고 있다.
# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 이때, 스택에 push하는 순서는 반드시 오름차순을
# 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop
# 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.

# 첫 줄에 n(1<=n<=100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1 이상 n 이하의 정수가 하나씩 순서대로 주어진다.
# 물론 같은 정수가 두 번 나오는 일은 없다.
# 입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push 연산은 +로, pop 연산은 -로 표현한다.
# 불가능한 경우 NO를 출력한다.

from collections import deque
n = int(input())
#li = [x for x in range(1, n+1)] # 들어가야할 수
#while len(li) :

# 1. 간접적으로 넣고 빼기
# 출력해야할 원소가 커지는 건 다 OK
# 출력해야할 원소가 작아질 경우, 내림차순에 맞는지 확인해야
# 내림차순이 아니면 오류 -> NO 출력
# output = []

'''
res = deque([])
max_a = 0 # queue에 append한 가장 높은 정수 저장
x_a = int(input()) # 첫 번째 원소 받기
for i in range(x_a) :
    res.append('+')
res.append('-')
max_a = x_a
for i in range(1, n) :
    print(res)
    a = int(input())
    if a > x_a and max_a < n : # a가 x_a보다 클 때
        for _ in range(abs(max_a - a)) :
            res.append('+')
        max_a = x_a = a
        continue
    elif a < x_a :
        for _ in range(abs(x_a - a)) :
            res.append('-') # 뺀 값들이 뭐뭐있는지 확인이 어려움 -> 실패 요인
        x_a = a
    else : # 내림차순에 해당하지 않는
        res.clear()
        break


if len(res) == 0 :
    print("NO")
else :
    while res :
        print(res.popleft())
'''



# 2. 직접 넣고 빼면서 확인하기
# top을 확인하면서 top이 내가 원하는 원소이면 빼고, 아니면 다른 원소 추가하기
# top이 내가 원하는 원소 또는 원소보다 크다 : stack에 있으면서 내가 뺄 수 있는 것
# top이 내가 원하는 원소보다 작다 : 추가할 원소가 아직 남아있다
# * 무조건 다 빼는 형태이기 때문에, top과 일치하지 않으면 그냥 실패?
# li = [x for x in range(1, n+1)]
# print(li)
# output = deque(li)
q = deque([])
res = deque([])

# 첫번째 queue 채우기
output = deque([])
for _ in range(n) :
    output.append(int(input()))
low = 1 # 여기부터 넣으면 된다
# high = obj # 맨 위에 있는 값 저장

while output :
    obj = output.popleft()

    for i in range(low, obj+1) :
        q.append(i)
        res.append('+')
    low = max(low, obj+1)

    print(q)
    top = q.pop()
    if top == obj :
        res.append('-')
    elif obj > top :
        q.append(top)
        for i in range(low, obj+1) :
            q.append(i)
            res.append('+')
        low = max(low, obj+1)
    else :
        res.clear()
        break
    


if len(res) == 0 :
    print("NO")
else :
    while res :
        print(res.popleft())



    
