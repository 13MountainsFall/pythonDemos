color_list = ["黑桃", "红桃", "梅花", "方片"]

num_list = range(1, 14)  # 左闭右开

card_list = []

# A 2 3 4 5 6 7 8 9 10 J P K Queen
for color_i in color_list:
    temp_card_list = []
    for num_i in num_list:
        temp_card_list.append((color_i, num_i,))
    card_list.append(temp_card_list)

for i in card_list:
    print(i)


l = list()
t = (1, 2, 3)

l.append(1)
l.append(2)
print(type(t))





