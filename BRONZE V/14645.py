# 성공
# 문제가 뭘 얘기하고 싶은 걸까?

# 버스 운전수 비와이 씨가 운전하는 버스(verse아님 ㅎ)는 N개의 정거장을 거친 후 종착역에 도착한다.
# 각 정거장은 내릴 인원수와 올라탈 인원수가 정해져 있다.
# 종착역에 도착하면 버스에 타고 있던 모든 사람이 내린다.

N, K = map(int, input().split())
for i in range(N) :
    add, sub = map(int, input().split())
    K=K+add-sub
print("비와이")