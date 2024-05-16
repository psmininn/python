# # 1.문자열 뒤집기
# # 문제: 문자열 my_string 이 매개변수로 주어집니다. my_string 을 거꾸로 뒤집은 문자열을 return 하도록 함수를 완성해주세요.
#
# def reversedWord(my_string):
#     wordList = list(my_string)
#     wordList.reverse()
#     reversedWord = "".join(wordList)
#     return reversedWord
#
# print(reversedWord("korea"))
#
# #2. 미완성된 할 일 찾기
# # 문제: todo_list 에 있는 할 일중, finished 배열을 통해 아직 끝내지 못한 일들은 찾아 순서대로 배열에 담아 반환 하는 함수를 만드세요!
#
# todoList = ["problem solving","practice guitar","swim","study graph"]
# doneList = [True,False,True,False]
#
# def filterDoneList(todoList, doneList):
#     return[item for index, item in enumerate(todoList) if doneList[index] == True]
#

# ----------------------------------------------------------------------------------------

class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def eat(self):
        print("냠냠냠")

    def sound(self):
        pass

    def introduce(self):
        print (f"안녕하세요! 저의 이름은'{self.name}'이고, 종은'{self.breed}' 입니다.")


class Dog(Animal):
    def sound(self):
        print("멍멍")


# 고양이 eat 냠냠냠 sound 냐옹

class Cat(Animal):
    def sound(self):
        print("냐옹")

# 퀴즈
# 관리자, 편집자, 뷰어 라는 각각 사용자가 존재합니다.
# 모두 접근하기라는 함수를 가지고 있습니다.
# 모두 username 이라는 속성도 가지고 있습니다.

# 관리자 - 유저만들기
# 편집자 - 편집하기
# 뷰어 - 조회하기

class User:
    def __init__(self, username):
        self.username = username

    def access(self):
        pass

class Admin:
    def access(self):
        print("관리자가 접근합니다.")

    def createUser(self):
        print("유저를 만들었습니다.")


class Editor(User):
    def access(self):
        print("편집자가 접근합니다.")

    def edit(self):
        print("편집을 합니다.")


class Viwer(User):
    def access(self):
        print("뷰어가 접근합니다.")

    def view(self):
        print("조회를 합니다.")









