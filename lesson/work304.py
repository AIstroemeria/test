def findkw(kw, tmpdir, flag):
    for items in os.listdir(tmpdir):
        if os.path.splitext(items)[1] == '.py':
            f = open(os.path.join(tmpdir, items),'r',encoding='UTF-8')
            lc = 0
            times = 0
            for lines in f:
                lc += 1
                pos = []
                while kw in lines:
                    if times == 0:
                        print('===============================================')
                        print('在文件【%s】中找到关键字【%s】' % (os.path.join(\
                            tmpdir,items), kw))
                    times += 1
                    pos.append((lines.find(kw)+len(pos)*len(kw)))
                    lines = lines[(lines.find(kw) + len(kw)):]
                if pos != []:
                    if flag:
                        print("关键字出现在第%d行，第" % lc,pos,"个位置。")
            f.close()
        elif os.path.isdir(os.path.join(tmpdir,items)):
            findkw(kw, os.path.join(tmpdir,items), flag)
        else:
            pass
                
        

import os
kw = input("请将该脚本放于待查找的文件夹内，请输入关键字:")
flag = input("请问是否需要打印关键字【%s】在文件中的具体位置（y/n):" % kw)
flag = True if flag == 'y' else False
findkw(kw, os.getcwd(), flag)
