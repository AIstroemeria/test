temp = input("请输入需要检查的密码组合：")
print("您的密码安全按级别评定为：",end="")
if len(temp) >= 8:
    count1 = 0
    for i in "~!@#$%^&*()_=-/,.?<>;:[]{}|\\":
        count1 += temp.find(i)
    count2 = 0
    for i in "123456789":
        count2 += temp.find(i)
    count3 = 0
    for i in "abcdefghigklmnopqrstuvwxyz":
        count3 += temp.find(i)
    if (count1 > -28) + (count2 > -10) + (count3 > -26) == 2:
        print("中")
        print("请按照以下方式提升您的密码安全级别")
        print("        1.密码必须由数字、字母及特殊字符三种组合")
        print("        2.密码只能由字母开头")
        print("        1.密码长度不能低于16位")
    elif (count1 > -28) + (count2 > -10) + (count3 > -26) == 3 and len(temp) >= 16:
        print("高")
        print("请继续保持")
    elif temp.isalnum() == True:
        print("低")
        print("请按照以下方式提升您的密码安全级别")
        print("        1.密码必须由数字、字母及特殊字符三种组合")
        print("        2.密码只能由字母开头")
        print("        1.密码长度不能低于16位")
    else:
        print("不合法!")
else:
    if temp.isalnum() == True:
        print("低")
        print("请按照以下方式提升您的密码安全级别")
        print("        1.密码必须由数字、字母及特殊字符三种组合")
        print("        2.密码只能由字母开头")
        print("        1.密码长度不能低于16位")
    else:
        print("不合法!")     
        
