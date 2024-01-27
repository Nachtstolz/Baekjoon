# 2920 # 성공!
# 음계

# 다장조는 c d e f g a b C, 총 8개 음으로 이루어져 있다. 이 문제에서 8개 음은
# 다음과 같이 숫자로 바꾸어 표현한다. c는 1로, d는 2로, ..., C를 8로 바꾼다.
# 1부터 8까지 차례대로 연주하면 ascending, 8부터 1까지 차례대로 연주하면 descending, 
# 둘 다 아니라면 mixed 이다.
# 연주한 순서가 주어졌을 때, 이것이 ascending, descending, mixed인지 판별하는 프로그램을 작성하라.

# 첫째 줄에 8개 숫자가 주어진다. 이 숫자는 문제 설명에서 설명한 음이며, 1부터 8까지 숫자가 한 번씩 등장한다.

arr = list(map(int, input().split()))
res = 0
if arr[0] == 1 :
    for i in range(1, len(arr)) :
        if arr[i] != arr[i-1]+1 :
            res = 3
            break
        res = 1
elif arr[0] == 8 :
    for i in range(1, len(arr)) :
        if arr[i] != arr[i-1]-1 :
            res = 3
            break
        res = 2
else :
    res = 3

if res == 1 :
    print("ascending")
elif res == 2 :
    print("descending")
else :
    print("mixed")
