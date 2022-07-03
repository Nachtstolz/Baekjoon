# 1541
# 잃어버린 괄호
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
# 첫째 줄에 식이 주어진다. 식은 '0~9', '+' 그리고 '-'만으로 이루어져있고,
# 가장 처음과 마지막 문자는 숫자이다.
# 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다.
# 수는 0 으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다

#exp = list(input())
exp = list(input())
print(exp) # 디버깅

min = 0
num = []
li = []

for i in range(len(exp)) :
    print('i : ', i) # 디버깅
    num.append(exp[i])
    
    if exp[i] == '+' or exp[i] == '-' :
        del num[-1]
        
        num_str = ''
        for j in range(len(num)) :
            num_str += num[j]
        li.append(int(num_str))
        
        print('num : ', num) # 디버깅
        print('li : ', li) # 디버깅
        
        li.append(exp[i])
        print('li : ', li) # 디버깅
        num = []
    
    if i == len(exp)-1 :
        num_str = ''
        for j in range(len(num)) :
            num_str += num[j]
        li.append(int(num_str))
    print(li)
    
    
    

    

