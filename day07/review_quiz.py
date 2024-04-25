#1. 문자열 문자 반복 프로그램
# 주어진 문자열 word 의 각 문자를 정수 n 만큼 반복하여 새로운 문자열을 생성 하는 프로그램을 작성하세요.

# word = input("문자 입력: ")
# count = int(input("반복할 횟수 입력: "))
#
# NewWord = ""
# for x in word:
#     NewWord += x * count
# print(NewWord)

#2. 모음 대문자화 문자열을 입력받아, 그 문자열 내의 모든 모음(a,e,i,o,u) 만 대문자로
#변환하는 프로그램을 작성하세요. 다른 문자들은 원래의 상태를 유지합니다. 이프로그램은
#문자열을 처리하여 모음만을 강조하는 방법을 보여줍니다.

# Newword = ""
# word = input("문자 입력: ")
#
# for x in word:
#     if x in "aeiou":
#         Newword += x.upper()
#     else:
#         Newword += x
# print(Newword)


#3.
#입력 : "cccCCC"
#출력 : "CCCccc"
#
# Newword = ""
# word = input("문자 입력: ")
# for x in word:
#     if x.isupper():
#         Newword += x.lower()
#     elif x.islower():
#         Newword += x.upper()
# #   else:
# #       Newword += x.upper()
# print(Newword)

# 단어를 입력했을 때
# 자음은 대문자화 해서 출력하기
# ex) hello -> HeLLo

# Newword = ""
# word = input("Enter a word: ")
#
# for x in word:
#     if x not in "aeiou":
#         Newword += x.upper()
#     else:
#         Newword += x
# print(Newword)



