
while True:
    temp = input("请输入一个整数（输入Q结束程序）：")
    if temp == "Q":
        break
    if temp.isdigit() == False:
        print("错误！")
        continue
    else:
        temp = int(temp)
        print("十进制  -> 十六进制：%d -> %#x" %(temp,temp))
        print("十进制  -> 八进制：%d -> %#o" %(temp,temp))
        print("十进制  -> 二进制：%d -> %s" %(temp,bin(temp)))
