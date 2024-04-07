# 需要十进制作为桥梁

a = bin(25)
b = oct(25)
c = hex(25)

d = int(str(c), base=16)  # 还原成十进制

print("二进制:{}\n八进制:{}\n十六进制:{}\n".format(a, b, c))  # {}:{}:{} 0b11001 0o31 0x1
print(d)
