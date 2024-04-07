a = "你好".encode("utf-8")
print(a)  # b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(a.decode("utf-8"))  # 你好

msg = "你好 abc"
msg_data = msg.encode("utf-8")
fd = open("1.txt", "wb")
fd.write(msg_data)
fd.close()

# 字符串类型
name = "武沛齐"

print(name)  # 武沛齐
# 字符串转换为字节类型
data = name.encode("utf-8")
print(data)  # b'\xe6\xad\xa6\xe6\xb2\x9b\xe9\xbd\x90'

# 把字节转换为字符串
old = data.decode("utf-8")
print(old)

# 字符串类型
name = "武沛齐"
print(name)  # 武沛齐
# 字符串转换为字节类型
data = name.encode("gbk")
# print(data) # b'\xe6\xad\xa6\xe6\xb2\x9b\xe9\xbd\x90'  utf8，中文3个字节
print(data)  # b'\xce\xe4\xc5\xe6\xc6\xeb'               gbk，中文2个字节

# 把字节转换为字符串
old = data.decode("gbk")
print(old)


