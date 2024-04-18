# condition_elif.py
# num = int(input("점수 입력: "))
# if num >=90 :
#     print("A등급")
# elif num >=80 :
#     print("B등급")
# elif num >=70 :
#     print("C등급")
# else:
#     print("과락입니다.")

# 국, 영, 수 점수를 3개 입력받고,
# 평균이 90 점 이상 'A', 80점 이상'B', 70점이상'C', 60점이상 'D'
# 나머지는 F로 나타내는 프로그램 작성하기

# test1 = input("국어점수 : ")
# test2 = input("영어점수 : ")
# test3 = input("수학점수 : ")
# avg = (int(test1) + int(test2) + int(test3)) / 3
# if avg >= 90 :
#     print("A등급")
# elif avg >= 80 :
#     print("B등급")
# elif avg >= 70 :
#     print("C등급")
# elif avg >= 60 :
#     print("D등급")
# else:
#     print("F등급")

# nested condition
# if문의 depth는 2번까지 지향하는 걸로!
score = int(input("점수 입력: "))
if score > 60 :
    if score ==100 :
        print("만점입니다")
    else:
        print("합격입니다")
else:
    if score == 0 :
        print("이건 좀..")
    else:
        print("불합격입니다")

