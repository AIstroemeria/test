def int_input(str):
    while True:
        try:
            tmp = input(str)
            res = int(tmp)
            return res
        except ValueError:
            print("出错，您输入的不是整数！")

int_input("请输入一个整数：")
