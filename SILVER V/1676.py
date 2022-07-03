# 1676 # 성공
# 팩토리얼 0의 개수
# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는
# 프로그램을 작성하시오

n = int(input())
res = 1 # 팩토리얼 결과 저장 변수
idx = 0 # 최종 결과 변수

# 팩토리얼 함수
for i in range(1, n+1) :
    res *= i

# 팩토리얼 결과 리스트에 저장
li = list(map(int, str(res)))

# 리스트 돌면서 0 값과 idx 확인
for i in range(len(li)-1, 0, -1) :
    if li[i] == 0 :
        continue
    else :
        idx = len(li)-1-i
        break
print(idx)