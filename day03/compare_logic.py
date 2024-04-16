#compare_logic.py
# >, <, <=, >=, ==[같니?], !=[다르니?]
a = 10
b = 20
print(a > b) # False
print(a >= b) # False
print(a < b) # True
print(a <= b) #True
print(a == b) # False
print(a != b) # True

#logic[논리] 연산자: bool 타입에 사용되는 연산자
# and, or, not
c=5
d=3
#and: 모든 조건이 참이면 참
print(c > d and c == d and d == 3) #True
#or : 하나라도 조건이 참이면 참
print (c < d or c == 6 or d == 3) #True
#not: 조건의 반대를 반환
print(not(c > d)) #False


x = 5
result = (x > 3) and x == 5
# 드모르간 법칙 적용
result1 = not(x <= 3) or x not(x != 5)