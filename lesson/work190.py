def whehuiwen(str1):
    if len(str1) <= 1:
        return True
    else:
        if str1[0] == str1[-1]:
            return whehuiwen(str1[1:-1])
        else:
            return False

temp = input("请输入一句话:")
res = whehuiwen(temp)
if res:
    print("是回文联！")
else:
    print("不是回文联！")
