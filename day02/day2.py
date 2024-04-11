# 콘솔창에
# language = "한국어"
# print(f"지금 설정한 언어는 {language}")

# 콘솔창에 유저에게 글을 입력 받는 기능 inp
# number = input("좋아하는 번호는?")
# print(f"좋아하는 번호는 {number}")

# 1. 어제의 일기 프로그램

date = input("날짜 입력:")
event = input("주요 사건입력:")
print(f"어제는{date},  주요사건은 {event}였습니다!")

# 2.오늘의  날짜와 아침, 점심, 저녁에 먹은 메누를  입력받아, '오늘은[날짜],  아침에는 [아침메뉴],
# 점심에는 [점심메뉴], 저녁에는 [저녁 메뉴]를 먹었습니다.' 라고 알려주는 프로그램을 작성 해보세요!

date = input("오늘의 날짜?")
morning = input("오늘의 아침메뉴는?")
lunch = input("오늘의 점심메뉴는?")
dinner = input("오늘의 저녁메뉴는?")
print(f"오늘은 {date}, 아침에는  {morning}, 점심에는 {lunch}, 저녁에는  {dinner}을 먹었습니다")
