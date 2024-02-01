# 8958 # 성공!
# OX퀴즈

# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
# 문제를 맞은 경우 그 문제의 점수는 문제까지 연속된 O의 개수가 된다. 예를 들어 10번 문제 점수는 3이다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
# OX퀴즈의 결과가 주엉졌을 때, 점수를 구하는 프로그램을 작성하라.
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고,
# 길이가 0보다 크고 80보다 작은 문자열이 주어진다.

t = int(input())
while t > 0 :
    t-=1
    str = list(input())
    num = 1 # O가 연속으로 나온 횟수
    score = 0 # 점수
    for i in range(len(str)) :
        if str[i] == 'O' :
            score += num
            num+=1
        else :
            num = 1
    print(score)