# 1991 # 성공 # 알고리즘 키워드 확인 후 풀이
# 트리 순회

# 이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal),
# 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 출력하시오.

# 첫째 줄에는 이진 트리의 노드의 개수 N(1<=N<=26)이 주어진다. 둘째 줄부터 N개의 줄에 거쳐 각 노드와 그의 왼쪽 자식 노드,
# 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다.
# 자식 노드가 없는 경우에는 .으로 표현한다.

# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다.
# 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

# 풀이) 서로소 집합 - 그래프 이론

n = int(input())
parent = [0] * n
for i in range(n) : # 부모 배열 초기화
    parent[i] = i

for _ in range(n) :
    a, b, c = input().split()
    if b == '.' and c == '.' :
        parent[ord(a)-65] = (-1, -1) # 자식 노드가 없는 경우
    elif b == '.' :
        parent[ord(a)-65] = (-1, ord(c)-65)
    elif c == '.' :
        parent[ord(a)-65] = (ord(b)-65, -1)
    else : 
        parent[ord(a)-65] = (ord(b)-65, ord(c)-65)

#print(parent)

# 전위 순회
def pre_recursion(parent, idx) :
    print(chr(65+idx), end='')
    if parent[idx][0] == -1 and parent[idx][1] == -1 :
        return
    
    if parent[idx][0] != -1 :
        pre_recursion(parent, parent[idx][0])
    if parent[idx][1] != -1 :
        pre_recursion(parent, parent[idx][1])

# 중위 순회
def in_recursion(parent, idx) :
    if parent[idx][0] == -1 and parent[idx][1] == -1 :
        print(chr(65+idx), end='')
        return
    
    if parent[idx][0] != -1 :
        in_recursion(parent, parent[idx][0])
    print(chr(65+idx), end='')
    if parent[idx][1] != -1 :
        in_recursion(parent, parent[idx][1])
        #  print(chr(65+idx), end='')


# 후위 순회
def post_recursion(parent, idx) :
    if parent[idx][0] == -1 and parent[idx][1] == -1 :
        print(chr(65+idx), end='')
        return
    
    if parent[idx][0] != -1 :
        post_recursion(parent, parent[idx][0])
    if parent[idx][1] != -1 :
        post_recursion(parent, parent[idx][1])
    print(chr(65+idx), end='')


pre_recursion(parent, 0)
print()
in_recursion(parent, 0)
print()
post_recursion(parent, 0)