file_name = input("请输入文件名：")
f = open(file_name, 'w')
print("请输入内容【单独输入':w'保存退出】：")
conts = []
while True:
    temp = input()
    if temp == ':w':
        f.writelines(conts)
        f.close()
        break
    conts.append(temp)
