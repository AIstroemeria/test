dict1 = {}
def working():
    while True:
        print('\n','''|--- 新建用户：N/n ---|
|--- 登陆账号：E/e ---|
|--- 退出程序：Q/q ---|''')
        orde = input("|--- 请输入指令代码:")
        if orde == 'N' or orde == 'n':
            key1 = input("请输入用户名：")
            while key1 in dict1:
                key1 = input("此用户名已被使用，请重新输入：")
            key2 = input("请输入密码：")
            dict1.setdefault(key1,key2)
            print("注册成功，赶紧登陆试试吧")
        elif orde == 'E' or orde == 'e':
            key1 = input("请输入用户名：")
            while key1 not in dict1:
                key1 = input("您输入的用户名不存在，请重新输入：")
            key2 = input("请输入密码：")
            if key2 == dict1[key1]:
                print("欢迎进入！")
            else:
                print("密码错误！")
        elif orde == 'Q' or orde == 'q':
            break
        else:
            print("错误指令")

working()
