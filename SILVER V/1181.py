# 1181 # 성공!
# 단어 정렬

''' 참고 자료 서치 후 결과 정리 '''
# sort에 조건을 기입 가능.
# arr.sort() # 알파벳 순서대로 정리
# arr.sort(key=len) # 문자열 길이 순서대로 정리
# 정렬 순서의 경우 상위 조건 A, 하위 조건 B가 있다면
# 먼저 B로 정렬한 후에 A로 정렬해야 원하는 결과 얻을 수 있음.
''' '''

# 알파벳 소문자로 이루어진 N 개의 단어가 들어오면 아래와 같은 조건에 따라 정렬.
# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로
# 단, 중복 단어는 하나만 남기고 제거.

# 첫째 줄에 단어 개수 N이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자 단어가
# 한 줄에 하나씩 주어짐. 주어지는 문자열 길이 50 넘지 않음.

n = int(input())
arr = []
for _ in range(n) :
    arr.append(input()) # 단어 입력받기

# 리스트 -> 세트, 세트 -> 리스트로 중복 제거되는지 확인하기
setted = set(arr)
res = list(setted)
n = len(res)
#print(n)

#print(res)
res.sort() # 정렬하기
#print(res)

# 단어 길이로 정렬
cnt = 0
for i in range(1, 51) :
    # 1. 길이가 x인 값들의 인덱스로 리스트 생성 -> 문자열 sort, 길이가 50까지 반복되도록
    # 2. len 1에서 50순서대로 가면서 sort된 리스트 내에서 하나씩 출력 -> len 리스트 필요 없음.
    # 2번으로 진행해보기로.

    if cnt == n :
        break
    for j in range(n) :
        if len(res[j]) == i :
            print(res[j])
            cnt+=1

