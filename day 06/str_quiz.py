#1. 뉴스 기사를 스크랩 해오고,
# 유저가 입력한 단어를 뉴스기사에서 그 해당 단어를 모두 대문자화 시켜서
# 다시 보여주기.

news = """Tesla has announced aggressive price cuts in China and Germany, 
shortly after reducing prices in the United States, 
as the world’s largest maker of electric vehicles
 (EV) faces declining sales and growing competition in major markets."""

word = input("Enter a word: ")
Newnew = news.replace(word,word.upper())
print(Newnew)




#2. 영어 기사를 스크랩 해오고,
#단어 사이에🍎 넣고 출력


a = news.split(" ")
b = "🍎".join(a)
print(b)

