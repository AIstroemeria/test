file_name1 = input("请输入需要比较的头一个文件名：")
file_name2 = input("请输入需要比较的另一个文件名：")
f1 = open(file_name1)
f2 = open(file_name2)
text1 = [l1 for l1 in f1]
print(text1)
text2 = [l2 for l2 in f2]
#默认行数一致
count = 0
errlist = []
for i in range(len(text1)):
    if text1[i] == text2[i]:
        continue
    count += 1
    tar = len(text1[i])
    for j in range(len(text1[i])):
        if text1[i][j] != text2[i][j]:
            tar = j
            break
    errlist.append((i,tar))

print("两个文件共有【%s】处不同" % count)
for i in range(count):
    print("第 %d 行第 %d 个字符开始不一样" % errlist[i])
        
