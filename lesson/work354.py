# -*- coding: utf-8 -*-
types = ['.m', '.c', '.cpp', '.py']

import easygui as g
import os
import sys
def countcode(pos, dict0, dict1):
    os.chdir(pos)
    for files in os.listdir():
        if files[0] == '.':
            continue
        if os.path.isdir(files):
            countcode(files, dict0, dict1)
            os.chdir(os.pardir)
        elif os.path.splitext(files)[1] in types:
            dict0.setdefault(os.path.splitext(files)[1],0)
            dict1.setdefault(os.path.splitext(files)[1],0)
            dict0[os.path.splitext(files)[1]] += 1
            with open(files,'r',encoding='utf-8',errors='ignore') as f:
                try:
                    temp = f.readlines()
                except:
                    print(os.path.join(os.getcwd(),files))
                    sys.exit(0)
                n = len(temp)
            dict1[os.path.splitext(files)[1]] += n


dict0 = {}
dict1 = {}
pos1 = g.diropenbox('请选择您的代码库：')
countcode(pos1, dict0, dict1)
while True:
    if g.boolbox('是否有其他目录？'):
        pos1 = g.diropenbox('请选择您的代码库：')
        countcode(pos1, dict0, dict1)
    else:
        break

msg1 = []
for i in  types:
    if i in dict0.keys():
        msg1.append('【%s】源文件%d个，源代码%d行' % (i, dict0[i], dict1[i]))
num = sum(dict1.values())
msg2 = '''您目前共累计编写了%d行代码，完成进度：%.2f%%
离10万行代码还差%d行，请继续努力!''' % (num, 100*num/1e5, 1e5-num)
g.textbox(msg = msg2, text=msg1)