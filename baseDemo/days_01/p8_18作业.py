"""
 商品列表：
      goods = [
    		{"name": "电脑", "price": 1999},
    		{"name": "鼠标", "price": 10},
    		{"name": "游艇", "price": 20},
    		{"name": "美女", "price": 998}
    	]
    要求:
    1：页面显示 序号 + 商品名称 + 商品价格，如：
          1 电脑 1999
          2 鼠标 10
    	  ...
    2：用户输入选择的商品序号，然后打印商品名称及商品价格
    3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
    4：用户输入Q或者q，退出程序。

"""


def goods():
    goods_list = [
        {"name": "电脑", "price": 1999},
        {"name": "鼠标", "price": 10},
        {"name": "游艇", "price": 20},
        {"name": "美女", "price": 998}
    ]

    template_m = "{} {} {}"
    dict_n = dict()
    for i in range(len(goods_list)):
        print(template_m.format(i + 1, goods_list[i].get("name"), goods_list[i].get("price")))
        dict_n[i + 1] = "{} {}".format(goods_list[i].get("name"), goods_list[i].get("price"))

    i_r = input("请输入商品编码：")
    if not i_r.isdecimal():
        print("输入不是数字")

    input_t = int(i_r)

    # print(dict_n)
    if input_t in dict_n:
        print("请确认您购买的商品：")
        print(input_t, dict_n.get(input_t))
    else:
        print("不存在该商品")


if __name__ == '__main__':
    goods()
