count = 0
"""
猜数字游戏
"""
while count < 3:
    inputA = int(input("please guess the age:"))
    if inputA == 14:
        print(f"u win")
        break
    else:
        print("u loss")
        if count == 2:
            print("over...")
    count += 1


