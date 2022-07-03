# 2675 # 정답
# 문자열 반복
# 첫째 줄에 테스트 케이스의 개수 T(1 <= T <= 1000)가 주어진다.
# 각 테스트 케이스는 반복 횟수 R(1 <= R <= 8), 문자열 S가 공백으로 구분되어 주어진다.
# S의 길이는 적어도 1이며, 20글자를 넘지 않는다.

t = int(input())
for i in range(t) :
    r, s = input().split()
    r = int(r) # 횟수는 int 형으로 저장
    s = list(s) # 문자열은 리스트로 저장
    for j in s :
        print(j*r, end='')
    print()
