# 12865 # DP # 해결법 논리 확인 후 풀이 # 성공!
# 평범한 배낭

# 한 달 후면 국가의 부름을 받게 되는 준서는 여행을 가려고 한다. 세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기에,
# 가지고 다닐 가방 또한 최대한 가치있게 싸려고 한다. 준서가 여행에 필요하다고 생각하는 N개의 물건이 있다.
# 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 았다.
# 아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 준서가 최대한 즐거운 여행을
# 하기 위해 넣을 수 있는 물건들의 가치와 최댓값을 알려주자.

# 첫 줄에 물품의 수 N(1<=N<=100)과 준서가 버틸 수 있는 무게 K(1<=K<=100,000)가 주어진다.
# 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게(1<=W<=100,000)와 해당 물건의 가치 V(0<=V<=1,000)가 주어진다.
# 입력으로 주어지는 모든 수는 정수이다.

n, k = map(int, input().split())
arr = []
res = [0] * (k+1)
for i in range(n) :
    w, v = map(int, input().split())
    arr.append((w,v))
# weight 기준으로 내림차순 sort
arr.sort(reverse=True)

for item in arr :
    #print(item)
    weight, value = item
    '''
    for idx in range(len(res)) :
        # idx 범위 체크
        # if idx >= weight*2 :
        #     break
        if idx-weight > 0 and res[idx-weight] == 0 :
            break
        # weight이 현재 갱신하려는 값의 idx 즉, 무게보다 작거나 같을 때 갱신 가능성 존재
        if weight <= idx :
            res[idx] = max(res[idx], res[idx-weight] + value)
        print(res)
    '''
    
    # 뒤에서부터 넣는 방식으로 변경
    for idx in range(len(res)-1, -1, -1) :
        if idx >= weight :
            res[idx] = max(res[idx], res[idx-weight] + value)

    #print(res)
# print(res[k])
print(max(res))

''' 인터넷 풀이법 : 냅색 알고리즘 '''
# ⭐️ 배낭 문제 : 배낭에 담을 수 있는 무게의 최댓값이 정해져 있고, 일정 가치와 무게가 있는 짐들을 배낭에 넣을 때,
# 가치의 합이 최대가 되도록 짐을 고르는 방법을 찾는 문제

# 배낭에 짐을 넣을 때, 짐을 쪼개서 넣을 수 있는 경우와 쪼개지 못하고 넣는 경우 두 가지가 존재.
# 쪼갤 수 있는 경우 '분할가능 배낭 문제' 쪼갤 수 없는 경우 '0-1 배낭 문제'라고 부른다.
# 쪼갤 수 없는 경우 "동적 계획법"으로 풀 수 있다.

# 알고리즘 설명 :
# x축엔 가방 1~K까지의 무게, y축은 물건 N개 개수만큼의 배열을 만들어준다. 행을 차례대로 돌며 다음과 같은 알고리즘을 수행한다.

# 1) 현재 물건이 현재 돌고있는 무게보다 작다면 바로 [이전물건][같은무게](knapsack[i-1][j])를 입력해준다.
# 2) 현재 물건을 넣어준다. 물건을 넣은 뒤의 남은 무게를 채울 수 있는 최댓값(knapsack[i-1][j-weight]을 위의 행에서
#   가져와 더해준다.
# 3) 현재 물건을 넣어주는 것보다 다른 물건들로 채우는 값(knapsack[i-1][j])을 가져온다.
# 2)와 3) 중 더 큰 값을 knapsack[i][j]에 저장한다. 이 값은 현재까지의 물건들로 구성할 수 있는 가장 가치 높은 구성이다.
# kanpsack[N][K]는 곧, K 무게일 때의 최댓값을 가리킨다.

'''
N, K = map(int, input().split())
stuff = [[0,0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))


#냅색 문제 풀이
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0] 
        value = stuff[i][1]
       
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])
'''