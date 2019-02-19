file_name = input("请输入要打开的文件：")
tar = input("请输入需要显示的行数：")
f = open(file_name)
text = [lines for lines in f]

if tar == ':':
    print("文件%s的全文的内容如下：" % file_name)
    tar1 = [0,len(text)]
else:
    tar1 = tar.split(':')
    tar2 = ['','']
    tar2[0] = '开始' if tar1[0] == '' else '第'+tar1[0]+'行'
    tar2[1] = '末尾' if tar1[1] == '' else '第'+tar1[1]+'行'
    print("文件%s从%s到%s的内容如下：" % (file_name, *tar2))
    tar1[0] = 0 if tar1[0] == '' else int(tar1[0])
    tar1[1] = len(text) if tar1[1] == '' else int(tar1[1])

for i in range(tar1[0]-1,tar1[1]):
    print(text[i])
