#1.1~100 까지의 총합을 나타내는 프로그램

# total = 0
# for x in range(1,101):
#     total = x + total # total += x
# print(total)

#2. 유저에게 과일을 입력 받고
#모음을 제거한 단어로 나타내기
# apple -> ppl, banana -> bnn

fruit =  input("과일 입력:")
word = ""
for x in fruit:
    if x != 'a' and x != 'e' and x != 'i' and x != 'o' and x != 'u':
    #if not x in 'aeiou':
        word += x
print(word)


