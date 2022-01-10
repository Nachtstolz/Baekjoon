# 성공

# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

a,b,c = map(int, input().split())
one = (a+b)%c
two = ((a%c) + (b%c))%c
three = (a*b)%c
four = ((a%c) * (b%c))%c

print(one)
print(two)
print(three)
print(four)