# 자료 구조: 데이터를 어떻게 보관하는지 다루는지에 대한 방법들
# list: 순서 있고 , 중복 가능
# set: 순서 없고, 중복 불가능
# dict: k[중복 안됨]-v[중복 가능] 형태로 저장
# tuple: (사과, 바나나, 키위) 수정 불가능



# 심화 자료 구조:
# graph: 그래프 자료구조 [지도, 미니맵, 경로 최적화 ]
# tree : 트리 자료구조 [단어 검색]

names = ['아메리카노','라뗴','바닐라']
prices =  [2000, 2500, 3000]
menu = []
for index,item in enumerate(names):
    menu.append({'name':item, 'price':prices[index]})
    print(menu[index])
# -> [{'name':'아메리카노','price':2000},{'name':'라뗴','price':2500}]

names = ['아메리카노','라뗴','바닐라']
prices =  [2000, 2500, 3000]

zipper
x =  dict(zip(names, prices))
print(x)

# 과일 이름 리스트:
# 과일 가격 리스트:
# zip으로 묶어서 k-v 형태 나타내세요.

furits = ['사과','바나나','키위']
prices = [2000, 2500, 3000]

menu = [{'name': x, 'price': y} for x, y in zip(furits, prices)]
print(menu)

for (x,y) in zip(furits,prices):
    print(f"{x},{y}")



for index, (x,y) in enumerate(zip(furits,prices)):
    print(f"{index}. {x}{y}")


name = ['아메리카노','라뗴','바닐라']
prices = [2000, 3000, 3500]

# => [{name:a,price:2000}]

menu = [{'name':x, 'prices':y} for (x,y) in zip(name, prices)]


#text = "apple banana apple strawberry banana"

#[{"단어":"apple","글자수":5},{"단어":"banana","글자수":6}...]

text = "apple banana apple strawberry banana"
a = [{"단어":x,"글자수":len(x)} for x in text.split(" ")]
print(a)

# 빅데이터: 코딩 - 통게 - 커뮤[영어] -> 뇌과학 + 교육
# 인공지능: 코딩 - 통게 - 커뮤[영어] -> 뇌과학 + 교육
# 뉴럴링크:






















