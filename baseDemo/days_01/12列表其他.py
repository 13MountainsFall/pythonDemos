import random

"""
注意本体操作与拷贝操作
"""
a = [1, 2]
b = ['qq', "123"]

c = a + b
print(c)

d = random.choice(c)
print(d)

# day8 下
user_list = ["王宝强", "陈羽凡", "Alex", "贾乃亮", "Alex"]
print(user_list)
print(user_list.pop(1))
print(user_list[2])
print(user_list.index("Alex"))
user_list.clear()
print(user_list)

# day7 sort
name = "王"
decimal_n = ord(name)
print(hex(decimal_n))  # 73 8b
print(bin(decimal_n))  # 0b 0111 0011 1000 1011

