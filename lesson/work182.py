targ = input("请输入目标字符串：")
mod1 = input("请输入子字符串：")
print('子字符串在目标字符串中共出现 %d 次' % findstr(targ,mod1))


########################
def findstr(str1,str2):
    count = 0;
    while True:
        temp = str1.find(str2)
        if temp == -1:
            break
        else:
            count += 1
            str1 = str1.partition(str2)[2]
    return count
    
