# 1978 # 성공
# 소수 찾기
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오

n = int(input())
li = list(map(int, input().split()))

cnt = 0 # 소수 여부를 판별하기 위한 변수
res = 0 # 최종 출력 변수
for i in li :
    if i == 1 :
        continue
    
    for j in range(1, i+1) :
        if i % j == 0 :
            cnt+=1
    if cnt == 2 :
        res+=1
    cnt = 0
print(res)