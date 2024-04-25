# data_type: int, str, float, bool, list
# list, set (집합)


# 중복 허용 안되는 타입
# a = {1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8}
# bugerking = {"새우와퍼","불고기와퍼","치즈와퍼","스테이크와퍼"}
# momstouch = {"새우와퍼","치즈와퍼","싸이버거","불고기버거"}
# x = bugerking.intersection(momstouch)
# print(x)

# 합집합 (|)
# union = bugerking | momstouch

# 교집합 (&)
# intersection = bugerking & momstouch
# intersection1 = bugerking.intersection(momstouch) # 위에 것이랑 차이 x

# 차집합 (-)


#추가
# burgerking =

# set()



news = """The company has suffered from falling demand and competition from cheaper Chinese imports which has led its stock price to collapse by 43% over 2024.

Figures for the first quarter of 2024 revealed revenues of $21.3bn, down on analysts' predictions of just over $22bn.

But the decision by Tesla to bring forward the launch of new models from the second half of 2025 boosted its shares by nearly 12.5% in after-hours trading.

It did not reveal pricing details for the new vehicles.

However Mr Musk made clear he also grander ambitions, touting Tesla's AI credentials and plans for self-driving vehicles - even going as far as to say considering it to be just a car company was the "wrong framework."

"If somebody doesn't believe Tesla is going to solve autonomy I think they should not be an investor," he said.

Such sentiments have been questioned by analysts though, with Deutsche Bank saying driverless cars face "technological, regulatory and operational challenges."

Some investors have called for the company to instead focus on releasing a lower price, mass-market EV.

However, Tesla has already been on a charm offensive, trying to win over new customers by dropping its prices in a series of markets in the face of falling sales."""

wordList = news.split()
noDuplicationWords = list(set(wordList))
noDuplicationWords.sort()
print(noDuplicationWords)