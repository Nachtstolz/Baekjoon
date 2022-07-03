# 11866 # 성공
# 요세푸스 문제 0
# N과 K가 주어지면 (N, K) - 요세푸스 순열을 구하는 프로그램을 작성하시오

n, k = map(int, input().split())
queue = []
for i in range(n) :
    queue.append(i+1)
idx = 0
cnt = n
print('<', end='')
while len(queue) != 0 :
    # queue[idx]가 k개 만나면 dequeue
    idx = idx+k-1
    # idx가 범위를 넘어갈 때
    while idx >= cnt :
        idx = idx-cnt
    if len(queue) == 1 :
        print(queue[idx], end='')
    else :
        print(queue[idx], end=', ')
    del queue[idx]
    cnt-=1
print('>')
