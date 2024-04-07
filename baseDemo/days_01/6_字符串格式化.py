# %
# format(推荐)
# f

text = "%s, 90%%" %"a"
print(text)
text2 = "==={0}==={0}=====>{1}".format("qq", "aa")
print(text2)
a = "123"
text3 = f"hello {a}"
print(text3)

b = 32
print(f"{b:#b}")     # 0b100000
print(f"{b:#o}")     # 0o40
print(f"{b:#x}")     # 0x20

