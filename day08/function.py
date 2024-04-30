#함수 input -> output
# 마술상자 : [100 -> 500, 200 - > 1000, 300 -> x]
# f(x) => len(x), str(x), int(x), print(x), input(x)
# count("p")

def koreaIT(x):
    return x + " 코리아 아이티"

def add(x, y):
    return x + y
a = add(1,5)
print(a)

# 어떠한 단어를 넣었을 때, 그 단어가 5글자 이상이면,
# 글자가 길어요!, 아니면 글자가 짧아요!

def iswordLong(x):
    if len(x) >= 5:
        return "글자가 길어요!"
    else:
        return "글자가 짧아요!"

# 함수: input -> [로직] -> output

#5,
# abc(3,'😁')
# ['😁','😁','😁']

def add(x, y):
    return [y for x in range(x)]

a = add(6,"😁")
print(a)

# 🥚 🐣 🐥 🐓 🍗
# 🥚 -> 🐣
# 🐣 -> 🐥
# 🐥 -> 🐓
# 🐓 -> 🍗

def changeEmogi(x):
    if x == "🥚":
        return "🐣"
    elif x == "🐣":
        return "🐥"
    elif x == "🐥":
        return "🐓"
    elif x == "🐓":
        return "🍗"
    else:
        return "EORROR"

print(changeEmogi("ㅇ"))
