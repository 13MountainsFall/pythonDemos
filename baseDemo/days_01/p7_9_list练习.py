li_1 = [1, 2, 3]
li_2 = [1, 2, 3, 4]

set_1 = set(li_1)
set_2 = set(li_2)
ll1 = set_2 - set_1  # diff
ll2 = set_2 & set_1  # intersection
ll3 = set_2.union(set_1)  # |
print(ll1)
print(ll2)
print(ll3)

set_3 = {1, 2, 3, (1, 3), }  # 元组是可以的，子子孙孙都得遵守
print(set_3)
