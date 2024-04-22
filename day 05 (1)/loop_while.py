# loop_while.py
#
# x = 10
# while x > 0 :
#     print("hello")
#     x -= 1
#
# while True:
#     x = int(input("정수 입력"))
#     if x == 0:
#         break

# 1. 아이스 아메리카노
# 2. 아이스 라뗴

# while True:
#     x = int(input("정수 입력"))
#     if x == 0:
#         print("프로그램 종료")
#         break
#     elif x == 1:
#         print("아이스 아메리카노")
#     elif x == 2:
#         print("아이스 라뗴")

#1. python!
#2. java
#3. c ++
#4. 프로그램 종료
#5. 그 외는 숫자를 잘못 입력하였습니다.

# while True:
#     x = int(input("언어를 고르세요(1.python! 2.java 3.c++):"))
#     if x == 1:
#         print( "python!")
#     elif x == 2:
#         print("java")
#     elif x == 3:
#         print("c++")
#     elif x == 4:
#         print("프로그램 종료")
#         break
#     else:
#         print("숫자를 잘못 입력하였습니다.")

 # 계산기 프로그램
 # 유저에게 0.프로그램 종료 1.더하기 2.빼기 3.곱하기 4.제곱 5.나누기(몫)
 # 그 외 번호는 "번호 입력 오류"
 #1번 -> 두 정수를 입력하고, 더한 결과값이 나옴
 #2번 -> 두 정수를 입력하고 뺀 결과값이 나옴

# 1

while True:
    print("계산기 프로그램")
    x = int(input("언어를 고르세요(0.프로그램 종료 1.더하기 2.빼기 3.곱하기 4.제곱 5.나누기(몫)):"))
    a = int(input("첫 번째 정수 입력"))
    b = int(input("두 번째 정수 입력"))
    if x == 0:
        print("프로그램 종료")
        break
    if x == 1:
        print( a + b )
    elif x == 2:
        print( a - b )
    elif x == 3:
        print( a * b )
    elif x == 4:
        print( a ** b )
    elif x == 5:
        print( a % b )
    else:
        print("번호 입력 오류")
