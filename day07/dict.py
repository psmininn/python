# [], {}, {}
# dict: key[str,int] and 중복 안됨 - value: anytype
# lecture = {
#     "java": 1,
#     "python": 2,
#     "c": 3,
#     "javascript": 4,
# }
# print(lecture["python"])

# coffeShop = {
#     "starbucks": ["아메리카노", "라뗴","민트"],
#     "Megacoffee": ["아메리카노","라떼","꿀아메리카노"],
# }


coffeShopMenu = {
    "starbucks":[{"name":"아메리카노"},{"naem":"라떼"}],
    "megacoffe":[{"name":"메가리카노","price":2000},{"name":"메가라뗴"}]
}
print(coffeShopMenu["megacoffe"])