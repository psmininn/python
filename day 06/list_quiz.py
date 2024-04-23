#1. 유저에게 다섯개의 정수를 입력 받고, 리스트화한 다음
#각각 요소를 3배로 만든다음 출력하기
#ex) [5,1,2,5,19] => [15,3,6,15,57]

numlist = []
for x in range(5):
    num = int(input("Enter a number: "))
    numlist.append(num)
print(numlist)

newnumlist=[]
for x in numlist:
    num3 = (x*3)
    newnumlist.append(num3)
print(newnumlist)



#2. 유저에게 서로 다른 다섯개의 정수를 입력 받고,
#리스트화 한 다음에, 가장 큰 수를 뽑아내는 프로그램

numlist = []
for x in range(5):
    num = int(input("Enter a number: "))
    numlist.append(num)
numlist.sort()
numlist.reverse()
print(numlist[0])