# 2609 # 성공
# 최대공약수와 최소공배수

# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하라.
# 첫째 줄에 두 개의 자연수가 주어지고, 둘은 10,000 이하의 자연수이다.
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 두 수의 최소공배수를 출력한다.

a, b = map(int, input().split())

std = min(a, b) # 작은 수 출력
res1 = 0 # 최대공약수
res2 = 0 # 최소공배수

for i in range(std, 0, -1) :
    if a % i == 0 and b % i == 0 :
        res1 = i
        break
res2 = res1 * (a//res1) * (b//res1)

print(res1)
print(res2)