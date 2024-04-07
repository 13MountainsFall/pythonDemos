import this


def fun1():
    name = "裘千仞"
    name.replace("千", "1")
    data = name[::-1]
    print(name)  # 裘千仞
    print(data)


def list_fun():
    list = ["zhangsan", "lisi", "wangWu"]

    for i in range(len(list) - 1, -1, -1):
        print(list[i])
    set_a = {1, 2, "aaa", None}
    print(list[-1])
    # print(list[-100]) # list index out of range


# def iter():
#     list2 = ["zhangsan", "lisi", "wangWu"]
#     iter__ = list2.__iter__()
#     print(iter__.__next__())


if __name__ == '__main__':
    # fun1()
    list_fun()
    # iter()
