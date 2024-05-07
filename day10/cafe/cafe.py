#카페 판매 직원용 프로그램 개발 요청
# 안녕하세요,

# beverage = int(input("숫자 입력 (1.신메뉴 추가 2. 프로그램 종료): "))
#
# cafe = {
#     '아메리카노': '2000원',
#     '라떼' : '2500원',
#     '바닐라라떼' : '3000원',
# }
# if beverage == 1:
#     cafe[input('커피이름')] = input('가격')
#
# if beverage == 2:
#     print("프로그램 종료")
#
# print(cafe)

from coffee import Coffee

coffeeList = [{'name':'아메리카노','price': 2000},{'name':'라떼','price': 2500},{'name':'바닐라라뗴','price': 3000}]


while True:
    codeNumber = int(input("1. 커피 판매 2. 커피 추가 3. 프로그램 종료: "))
    if codeNumber == 1:
        coffeeNumber = int(input(coffeeList))
    elif codeNumber == 2:
        newCoffeeName  = input("커피이름:")
        newCoffeePrice = int(input("커피 가격:"))
        newCoffeeMenu = {"name":newCoffeeName,"price":newCoffeePrice}
        coffeeList.append(newCoffeeMenu)
        print(f"{coffeeList}가 추가되었습니다.")
    elif codeNumber == 3:
        print("프로그램 종료")
        break
