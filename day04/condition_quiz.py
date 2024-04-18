#1. 정수를 입력 받고
# 양의 홀수 , 양의 짝수, 0, 음의 홀수, 음의 짝수
#판별해주는 프로그램
# ex) -5 => 음의 홀수, 0 => 0, 3 => 양의 홀수

# num= int(input("Enter a number: "))
# if num > 0:
#     if num % 2 == 0:
#         print("양의 짝수")
#     else:
#         print("양의 홀수")
# elif num == 0:
#     print("0")
# else:
#     if num % 2 == 0:
#         print("음의 짝수")
#     else:
#         print("음의 홀수")

# 다른방법( 심화방법 )
# num= int(input("Enter a number: "))
# isPositive = num > 0
# isNegative = num < 0
# isOdd = num % 2 == 1
# isEven = num % 2 == 0
# if isPositive and isOdd:
#     print("양의 홀수 입니다.")
# elif isPositive and isEven:
#     print("양의 짝수 입니다.")
# elif isNegative and isOdd:
#     print("음의 홀수 입니다.")
# elif isOdd and isEven:
#     print("음의 짝수 입니다.")
# else:
#     print("0입니다.")

#좌표 평면에서 위치 판별 프로그램
# 사용자로부터 x축과 y축의 좌표값 x와 y를 입력받아, 해당 좌표가 좌표 평면의 어느 사분면에 위치하는지
#판별하는 프로그램을 만들어보세요. 좌표가 각각의 사분면에 위치하는 경우, '입력하신 좌표는 제1사분면에 위치합니다.'
#등과 같이 출력하고, 좌표가 축 위에 있는 경우는 'x축 위에 위피합니다.','원점에 위치합니다.' 등과 같이
#구체적으로 알려주는 프로그램을 작성해보세요!

# X = int(input("X좌표 값을 입력: "))
# Y = int(input("Y좌표 값을 입력: "))
#
# isXPositive = X > 0
# isXNegative = X < 0
# isXZero = X == 0
# isYPositive = Y > 0
# isYNegative = Y < 0
# isYZero = Y == 0
#
# if isXZero and isYZero:
#     print("원점입니다.")
# elif isXZero:
#     print("Y축 위에 존재합니다.")
# elif isYZero:
#     print("X축 위에 존재합니다.")
# elif isYPositive and isXPositive:
#     print("1사분면 위에 존재합니다.")
# elif isXPositive and isYNegative:
#     print("4사분면 위에 존재합니다.")
# elif isYPositive and isXNegative:
#     print("2사분면 위에 존재합니다.")
# else:
#     print("3사분면 위에 존재합니다.")

#4. 마트 할인 적용 프로그램
# 사용자로부터 마트에서 구매한 총 금액을 입력받아, 그 금액에 따라 할인율을 적용하는 프로그램을 만들어보세요.
# 구매 금액이 50,000원 이상이면 5%, 100,000원 이상이면 10%, 200,000원 이상이면 20%의 할인을 적용합니다.
# 사용자가 입력한 금액에 따라 적용된 할인율과 할인된 금액을 계산하여 '구매 금액은[원본금액]원, 할인율은 [할인율%]
# 할인금액]원, 최종결제 금액은 [최종금액]원 입니다. 라고 결과를 출력하는 프로그램을 작성ㅅ해 보세요.

price = int(input("금액 입력: "))

if price >= 200000:
    print(f"구매 금액은[{price}]원, 할인율은 [{20}]%, 할인 금액은 [{price*0.2}]원, 최종결제 금액은 [{price - price*0.2}]원 입니다.")
elif price >= 100000:
    print(f"구매 금액은[{price}]원, 할인율은 [{10}]%, 할인 금액은 [{price*0.1}]원, 최종결제 금액은 [{price - price*0.1}]원 입니다.")
elif price >= 50000:
    print(f"구매 금액은[{price}]원, 할인율은 [{5}]%, 할인 금액은 [{price * 0.05}]원, 최종결제 금액은 [{price - price*0.05}]원 입니다.")
else:
    print(f"구매 금액은[{price}]원, 할인율은 [{0}]%, 할인 금액은 [{price * 0}]원, 최종결제 금액은 [{price - prcie*0}]원 입니다.")


