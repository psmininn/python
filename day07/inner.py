# "hello".upper() => HELLO
#

# length
# len : 문자열 또는 리스트의 길이를 알려주는 기능
# print(len("hello"))
# print(len("python"))
# print(len([2,3,4,5,6,7]))
#
# # max, min
# print(max([1,2342,3523,5235,256,23]))
# print(min([1,2342,3523,5235,256,23]))
#
# #sum
# print(sum([1,2,3,4,5]))



#1. 영어 기사 스크랩 해오고, 단어 길이가 6글자 이상인
# 단어들만 출력하기

news ="""Tesla has announced its profits fell sharply in the first three months of the year to $1.13bn (£910m), compared with $2.51bn in 2023.

It caps a difficult period for the electric vehicle (EV) maker, which - faced with falling sales - has announced thousands of job cuts.

Boss Elon Musk remains bullish about its prospects, telling investors the launch of new models would be brought forward.

Its share price has risen but analysts say it continues to face significant challenges, including from lower-cost rivals."""


# newword = news.split(" ")
# newword.sort()
# print(newword)
# for x in newword:
#     if len(x) >= 6:
#         print(x)

fruits = ["apple", "banana", "kiwi", "mango","strawberry","pineapple","melon"]

# 문자 길이가 5글자 이하이고 알파벳 a,e 포함되면 대문자로 출력하고
#그게 아니면 그 과일의 문자 길이를 출력하는 프로그램

# - > APPLE, 6, 4, MANGO,...

for x in fruits:
    if len(x) <= 5 and ("a" in x or "e" in x):
        print(x.upper())
    else:
        print(len(x))


