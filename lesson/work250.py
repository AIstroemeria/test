print('''|--- 欢迎进入通讯录程序 ---|
|--- 1：查询联系人资料 ---|
|--- 2：插入新的联系人 ---|
|--- 3：删除已有联系人 ---|
|--- 4：退出通讯录程序 ---|''')
dict1 = dict()

while True:
    print("\n")
    orde = int(input("请输入相关指令代码:"))
    if orde == 1:
        key1 = input("请输入联系人姓名:")
        if key1 in dict1.keys():
            print(key1, ":", dict1[key1])
        else:
            print("查无此人！")
    elif orde == 2:
        key1 = input("请输入联系人姓名:")
        if key1 in dict1.keys():
            print("您输入的姓名在通讯录中已存在 -->>",key1,"：",dict1[key1])
            if input("是否修改用户资料（YES/NO):") == 'YES':
                key2 = input("请输入用户联系电话:")
                dict1[key1] = key2
            else:
                print("未进行修改")
        else:
            key2 = input("请输入用户联系电话:")
            dict1[key1] = key2
    elif orde == 3:
        key1 = input("请输入联系人姓名:")
        del dict1[key1]
    elif orde == 4:
        print("|--- 感谢使用通讯录程序 ---|")
        break
    else:
        print("无此命令！")
