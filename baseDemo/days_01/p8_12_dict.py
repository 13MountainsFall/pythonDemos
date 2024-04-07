def part_1():
    dict_1 = {
        "zjangsan": 123,
        "lisi": 123,
        "wanger": 123,
    }

    keys = dict_1.keys()
    print(type(keys))  # <class 'dict_keys'>

    s = set(keys)
    print("aaa" in s)

    l = list(s)
    l.pop(0)
    print(l)
    del dict_1['wanger']
    print(dict_1)


def part_2():
    li1 = [1, 2, 3]
    li2 = [1, 2, 3, 4]
    # li3 = li1 | li2  # unsupported operand type(s) for |: 'list' and 'list'
    # print(li3)


def del_f():
    a = 1
    print(a)
    l1 = [1, 2, 3]
    # print(a)
    del l1[1]
    print(l1)


def part2():
    m = "k1:2"
    k, v = m.split(":")
    print(f"{k} : {v}")


if __name__ == '__main__':
    # part_1()
    # part_2()
    # del_f()
    part2()
