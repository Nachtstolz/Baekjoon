# 1764 # 자료구조 # 문자열 # 정렬 # 해시 # 정답
# 듣보잡

# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과
# N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다.
# N, M은 500,000 이하의 자연수이다.
# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

# 듣보잡의 수와 그 명단을 사전순으로 출력한다.


n, m = map(int, input().split())

dic = {} # 해시
res = []
for i in range(n) :
    dic[input()] = 1
for j in range(m) :
    tmp = input()
    if tmp in dic.keys() :
        res.append(tmp)

print(len(res))
res.sort() # 정렬 속도 줄일 방법 찾기
for i in res :
    print(i)


''' set을 활용한 코드 : 서치 '''
n, m = map(int, input().split())

arr1 = []
arr2 = []

for i in range(n) :
    arr1.append(input())
for j in range(m) :
    arr2.append(input())

# set 교집합
answer = list(set(arr1) & set(arr2))
print(len(answer))
# 리스트 내 원소 한 번에 출력하기
# Asterisk(*)를 사용하면 리스트 압축 해제가 가능하기 때문
print(*sorted(answer), sep='\n')