#enumerate : 열거하다
# fruits = ['apple', 'orange', 'mango']
# for index,item in enumerate(fruits):
#     print(f"{index}.{item}")

# coffees = [{'name':'아메리카노','price':2000},{'name':'라떼','price':3000}]
# for index,item in enumerate(coffees):
#     print(f"{index}. {item['name']} {item['price']} 원")

coffeeList = [{'name':'아메리카노','price': 2000},{'name':'라떼','price': 2500},{'name':'바닐라라뗴','price': 3000}]


while True:
    codeNumber = int(input("1. 커피 판매 2. 커피 추가 3. 프로그램 종료: "))
    if codeNumber == 1:
        for index,item in enumerate(coffeeList):
            print(f"{index}. {item['name']} {item['price']} 원")
    elif codeNumber == 2:
        newCoffeeName  = input("커피이름:")
        newCoffeePrice = int(input("커피 가격:"))
        newCoffeeMenu = {"name":newCoffeeName,"price":newCoffeePrice}
        coffeeList.append(newCoffeeMenu)
        print(f"{newCoffeeName}가 추가되었습니다!")
    elif codeNumber == 3:
        print("프로그램 종료")
        break



