#comprehension
#[0~100]

# 0~ 100 까지의 숫자가 담긴 리스트 만들기 방법
# 1.
# numlist = []
# for x in range(101):
#     numlist.append(x)
# print(numlist)
#
# #2.
# a = [x for x in range(101)]
# print(a)
#
# # "apple" => [a,p,p,l,e]
# b = [x for x in "apple"]
# print(b)
#
# #0 ~ 10 짝수만 리스트
# c = [x for x in range(11) if x % 2 == 0]
# print(c)
#
# #0~100 홀수만 리스트
# d = [x for x in range(101) if x % 2 == 1]
# print(d)
#
# # 0~100 짝수를 제곱인 형태인 리스트
# e = [x ** 2  for x in range(101) if x % 2 == 0]
# print(e)
#
# # 0~10  홀수에서 10 을 더한 리스트
# #[11,13,15,17,19]
# f = [x + 10  for x in range(11) if x % 2 == 1]
# print(f)
#
# fruits = ["apple", "banana", "kiwi","grape","orange"]
# g = [len(x) for x in fruits if 'i' in x]
# print(g)
#
#
#
#
# #매핑 컴프리헨션
# #홀수는 10 짝수는 20
h = [x + 10 if x % 2 == 1 else x + 20  for x in range(101)]
print(h)



fruits = ["apple", "banana", "kiwi","grape","orange"]

# 5글자 이하이면 글자의 길이로 나타내고, 아니면 대문자화 히
a =  [len(x) if len(x) <= 5 else x.upper() for x in fruits]
print(a)

