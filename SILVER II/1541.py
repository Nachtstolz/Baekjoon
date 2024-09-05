# 1541 # 그리디 # 파싱 # 인터넷 자료 서치
# 잃어버린 괄호

# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
# 첫째 줄에 식이 주어진다. 식은 '0~9', '+' 그리고 '-'만으로 이루어져있고,
# 가장 처음과 마지막 문자는 숫자이다.
# 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다.
# 수는 0 으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다

#exp = list(input())
first = input()
exp = list(first)
# print(exp) # 디버깅

minus_li = first.split('-')
res = 0
for i in minus_li[0].split('+') :
    res+=int(i)

for each in minus_li[1:] :
    for j in each.split('+') :
        res-=int(j)

print(res)
# 인풋으로 받은 exp를 연산자와 숫자로 분리하는 과정
'''
minst = int(1e9)
num = []
li = []
# oper_cnt = 0
# num_cnt = 0

for i in range(len(exp)) :
    print('i : ', i) # 디버깅
    num.append(exp[i])
    
    if exp[i] == '+' or exp[i] == '-' :
        del num[-1]
        # oper_cnt+=1
        
        num_str = ''
        for j in range(len(num)) :
            num_str += num[j]
        li.append(str(int(num_str)))
        
        print('num : ', num) # 디버깅
        print('li : ', li) # 디버깅
        
        li.append(exp[i])
        print('li : ', li) # 디버깅
        num = []
    
    if i == len(exp)-1 :
        num_str = ''
        for j in range(len(num)) :
            num_str += num[j]
        li.append(str(int((num_str))))
    print(li) # 디버깅
    
    # num_cnt = len(li)-oper_cnt
'''

# 작은 괄호 -> 큰 괄호로 늘려가는 방식
'''
for i in range(0, len(li)-2,2) :
    li.insert(i, '(')
    for j in range(i+4, len(li)+1, 2) :
        li.insert(j, ')')
        print(li) # 디버깅
        tmp = ''.join(li)
        print(tmp) # 디버깅
        li.remove(')')
        minst = min(minst, eval(tmp))
        # print(minst)
    li.remove('(')
'''

# 큰 괄호 -> 작은 괄호로 줄여가는 방식
# 처음에 가장 큰 괄호 만들고 시작
'''
li.insert(0, '(')
li.append(')')
minst = min(minst, ''.join(li))

for i in range(1, num_cnt) :
    idx = 2
    while 
'''
