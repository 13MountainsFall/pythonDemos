# 元组
def part_1():
    a = (1, 2, 'aaa')
    b = (1, 2, 'aaa',)

    print(a == b)
    """
    声明
    """
    c = (1)
    d = (1,)

    print(type(c))
    print(type(d))

    # True
    # <class 'int'>
    # <class 'tuple'>

    """
    类型转换
    """
    name = "武沛齐"
    data = tuple(name)
    print(data)  # 输出 ("武","沛","齐")
    name = ["武沛齐", 18, "pythonav"]
    data = tuple(name)
    print(data)  # 输出 ("武沛齐",18,"pythonav")

    e = ()
    if not e:
        print("111111")

    v1 = [] or "alex"
    v2 = [11, 22] and (1, 2,)

    print(v1)
    print(v2)


# 7_10
def part_2():
    tuple_a = (1, 2, [1, 2, 3, 4])
    print(tuple_a[2])
    # tuple_a[2] = []  # 'tuple' object does not support item assignment
    tuple_a[2].append(1112)
    print(tuple_a)


def test_1():
    tu_01 = (False,)  # True
    bo_01 = bool(tu_01)
    print(bo_01)


if __name__ == '__main__':
    part_2()
    test_1()
