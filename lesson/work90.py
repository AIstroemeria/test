time = 3
while True:
    tmp = input("请输入密码：")
    while '*' in tmp:
        print("密码中不能含有“*”号！",end = '')
        tmp = input("您还有"+str(time)+"次机会！请输入密码:")
    if tmp == "qwerty":
        print("密码正确，进入程序......")
        break
    else:
        print("密码输入错误！",end = '')
    time -= 1;
    if time == 0:
        print("请稍后重试！")
        break
    else:
        print("您还有"+str(time)+"次机会！",end = '')
        
