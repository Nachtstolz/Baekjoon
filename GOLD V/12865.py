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