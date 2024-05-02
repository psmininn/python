# map(how, target): target을 바꿔주기
numlist = [x for x in range(10)]
# [100,101,102,103,...200]
result = list(map(lambda x: x * 2, numlist))
print(result)

#filter: target을 필터링 해줌
result1 = list(filter(lambda x: x % 2== 0 ,numlist))
print(result1)


fruits = ['apple', 'banana', 'cherry','kiwi']
result2 = list(filter(lambda x: len(x)<= 5 , fruits))
print(result2)

result3 = list(filter(lambda x: 'a' in x ,fruits))
print(result3)

emailList = ["abc@naver.com","mega@gmail.com","korea@daum.com"]
# map -> 유저아이디로 바꾸기

result = list(map(lambda x: x.split("@")[0], emailList))
print(result)

