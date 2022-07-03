# 1018 # 실패 # 예제 중 9 23 예제 어떻게... 한담
# 체스판 다시 칠하기
# 첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다.
# 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다.
# B는 검은색이며, W는 흰색이다.

n,m = map(int, input().split())
li = []
for i in range(n) :
    tmp = list(input())
    li.append(tmp)
# print(li)

# x : 2차원 배열의 열 부분 시작 인덱스
# y : 2차원 배열의 행 부분 시작 인덱스
x = 0
y = 0
# a : n의 열을 가진 배열이 도전해볼 수 있는 시작 인덱스 제한
# b : m의 행을 가진 배열이 도전해볼 수 있는 시작 인덱스 제한
a = n-8
b = m-8

cnt = 0
min = 0

while x<=a :
    y = 0
    while y<=b :
        print(f'x : {x}, y : {y}로 반복문 시작')
        if li[x][y] == 'B' :
            for i in range(8) :
                for j in range(8) :
                    if (i+j)%2 == 0 and li[x+i][y+j] == 'W' :
                        cnt+=1
                    elif (i+j)%2 == 1 and li[x+i][y+j] == 'B' :
                        cnt+=1
                    j+=1
                i+=1
        else :
            for i in range(8) :
                for j in range(8) :
                    if (i+j)%2 == 0 and li[x+i][y+j] == 'B' :
                        cnt+=1
                    elif (i+j)%2 == 1 and li[x+i][y+j] == 'W' :
                        cnt+=1
                    j+=1
                i+=1
        print('cnt : ', cnt)
        if x == 0 and y == 0 :
            min = cnt
        elif min > cnt :
            min = cnt
        cnt = 0
        y+=1
    x+=1
            
print(min)