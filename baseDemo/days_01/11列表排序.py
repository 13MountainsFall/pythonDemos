def f1():
    user_list = ["王宝强", "Ab陈羽凡", "Alex", "贾乃亮", "贾乃", "1"]
    user_list2 = [29579, 23453, 24378]
    #       [29579, 23453, 24378]
    #       [65, 98, 38472, 32701, 20961]
    #       [65, 108, 101, 120]
    #       [49]
    # print(user_list)
    """
    sort的排序原理
        [ "x x x" ," x x x x x " ]
    """
    user_list.sort()
    print(user_list)
    user_list2.sort()
    print(user_list2)

    user_list = ["王宝强", "陈羽凡", "Alex", "贾乃亮", "Alex"]
    user_list.reverse()
    print(user_list)

    for i in range(10, -1, -1):
        print(i, end="\t")


# void sort
def f2():
    ll = [1, 3, 2]
    ll.sort()
    print(ll)
    l2 = ll + [-1]
    l2.sort()
    print(l2)


if __name__ == '__main__':
    # f1()
    f2()
