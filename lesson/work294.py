filename = input("请输入文件名：")
change1 = input("请输入需要替换的单词或者字符：")
change2 = input("请输入新的单词或字符：")

f = open(filename)
text = f.read()
f.close()
counts = text.count(change1)
print("文件%s中共有%d个【%s】" % (filename, counts, change1))
print("您确定要把所有的【%s】替换为【%s】吗？" % (change1,change2))
res = input("y/n:")
if res == 'y':
    text = text.replace(change1, change2)
    f = open(filename,'w')
    f.write(text)
    f.close()
